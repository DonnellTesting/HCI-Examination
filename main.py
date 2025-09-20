def gps_tracker():
    """
    A simple GPS tracker simulator that tracks player movement on a 2D coordinate system.
    Player starts at origin (0, 0) and moves based on directional commands.
    """
    # Initialize starting position
    x, y = 0, 0
    
    print("=== GPS Tracker Simulator ===")
    print(f"Starting position: ({x}, {y})")
    print("\nCommands:")
    print("  N or n or North or north = Move North (y+1)")
    print("  S or s or South or south = Move South (y-1)")
    print("  E or e or East or east = Move East (x+1)")
    print("  W or w or West or west = Move West (x-1)")
    print("  STOP = End session")
    print("-" * 40)
    
    while True:
        # Get user input
        command = input("\nEnter command: ").strip()
        
        # Check for stop condition
        if command.upper() == "STOP":
            break
        
        # Process movement commands (handle various valid inputs)
        command_upper = command.upper()
        if command_upper in ["N", "NORTH"]:
            y += 1
            print(f"Moved North. Current position: ({x}, {y})")
        elif command_upper in ["S", "SOUTH"]:
            y -= 1
            print(f"Moved South. Current position: ({x}, {y})")
        elif command_upper in ["E", "EAST"]:
            x += 1
            print(f"Moved East. Current position: ({x}, {y})")
        elif command_upper in ["W", "WEST"]:
            x -= 1
            print(f"Moved West. Current position: ({x}, {y})")
        else:
            # Handle invalid input
            print("Invalid command! Please use N/North, S/South, E/East, W/West, or STOP")
    
    # Session ended - show final results
    print("\n" + "=" * 40)
    print("SESSION ENDED")
    print(f"Final position: ({x}, {y})")
    
    # Check if user returned to origin
    if x == 0 and y == 0:
        print("Congratulations! You returned to the origin (0, 0)!")
    else:
        print("You did not return to the origin (0, 0).")
    
    print("=" * 40)


# Alternative class-based implementation for better organization
class GPSTracker:
    """
    Object-oriented version of the GPS tracker simulator.
    """
    
    def __init__(self):
        """Initialize tracker at origin."""
        self.x = 0
        self.y = 0
        self.move_history = []
    
    def get_position(self):
        """Return current position as tuple."""
        return (self.x, self.y)
    
    def move_north(self):
        """Move one unit north (increase y)."""
        self.y += 1
        self.move_history.append("North")
        return self.get_position()
    
    def move_south(self):
        """Move one unit south (decrease y)."""
        self.y -= 1
        self.move_history.append("South")
        return self.get_position()
    
    def move_east(self):
        """Move one unit east (increase x)."""
        self.x += 1
        self.move_history.append("East")
        return self.get_position()
    
    def move_west(self):
        """Move one unit west (decrease x)."""
        self.x -= 1
        self.move_history.append("West")
        return self.get_position()
    
    def is_at_origin(self):
        """Check if current position is at origin (0, 0)."""
        return self.x == 0 and self.y == 0
    
    def process_command(self, command):
        """
        Process a movement command and return the new position.
        Returns None for invalid commands.
        """
        command_upper = command.strip().upper()
        
        if command_upper in ["N", "NORTH"]:
            return self.move_north()
        elif command_upper in ["S", "SOUTH"]:
            return self.move_south()
        elif command_upper in ["E", "EAST"]:
            return self.move_east()
        elif command_upper in ["W", "WEST"]:
            return self.move_west()
        else:
            return None
    
    def run_simulation(self):
        """Run the interactive GPS tracker simulation."""
        print("=== GPS Tracker Simulator (OOP Version) ===")
        print(f"Starting position: {self.get_position()}")
        print("\nCommands:")
        print("  N or n or North or north = Move North")
        print("  S or s or South or south = Move South") 
        print("  E or e or East or east = Move East")
        print("  W or w or West or west = Move West")
        print("  STOP = End session")
        print("-" * 45)
        
        while True:
            command = input("\nEnter command: ")
            
            if command.strip().upper() == "STOP":
                break
            
            new_position = self.process_command(command)
            
            if new_position:
                direction = self.move_history[-1]
                print(f"Moved {direction}. Current position: {new_position}")
            else:
                print("Invalid command! Please use N/North, S/South, E/East, W/West, or STOP")
        
        # Show final results
        print("\n" + "=" * 45)
        print("SESSION ENDED")
        print(f"Final position: {self.get_position()}")
        print(f"Total moves made: {len(self.move_history)}")
        
        if self.is_at_origin():
            print("Congratulations! You returned to the origin (0, 0)!")
        else:
            print("You did not return to the origin (0, 0).")
        
        if self.move_history:
            print(f"Move history: {' -> '.join(self.move_history)}")
        
        print("=" * 45)


if __name__ == "__main__":
    # You can run either version:
    
    # Simple functional version
    print("Choose version:")
    print("1. Simple version")
    print("2. Object-oriented version")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        gps_tracker()
    elif choice == "2":
        tracker = GPSTracker()
        tracker.run_simulation()
    else:
        print("Invalid choice. Running simple version by default.")
        gps_tracker()
        
