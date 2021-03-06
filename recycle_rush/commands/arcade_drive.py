import wpilib
from wpilib.command import Command
from subsystems.drive import Drive

class ArcadeDrive(Command):
    '''
        Used to move the robot
    '''
    def __init__(self, drive, get_x, get_y):
        '''
            initializes arcade drive movement
            :param drive : instance of the class Drive
            :param get_x : can be a function or #
            :param get_y : 
        '''
        super().__init__()
        
        self.drive = drive
        self.get_x = get_x
        self.get_y = get_y
        self.requires(drive)
        
   
    def execute(self):
        '''
            Called repeatedly when this Command is scheduled
            to run
        '''
        x = self.get_x() if callable(self.get_x) else self.get_x
        y = self.get_y() if callable(self.get_y) else self.get_y
        self.drive.robot_move(0, y, x, 0)
        
        
    def isFinished(self):
        '''
            Make this return true when this Command no longer
            needs to run execute()
        '''
        return False
   
    def end(self):
        '''
            Called once after isFinished returns true
        '''
        self.drive.robot_move (0,0,0,0)
        
    def interrupted(self):
        '''
            Called when another command which requires one or
            more of the same subsystems is scheduled to run
        '''
        self.end()