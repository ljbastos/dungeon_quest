import random, os

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
        user_name: str = input("Enter your name: ")
        
        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        player: dict = {
            'name':user_name,
            'health':10,
            'inventory':[]
            }
        # TODO: Return the dictionary
        return player


    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        treasure = {
            "diamond": 10,
            "gold ring": 6,
            "amethyst": 5,
            "dusty map": 1,
            "shiny garnet": 9,
            "small healing potion": 3,
            "medium healing potion": 5,
            "big healing potion": 10
        }
        # TODO: Return the dictionary
        return treasure


    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room number and the 4 menu options listed above
        options = [
            'Search for treasure',
            'Move to next room',
            'Check health and inventory',
            'Quit the game'
            ]
        print("\033c", end="")
        print(f"\nYou are in room {room_number}.\n")
        print("What would you like to do?\n")
        for num in range(1,len(options)+1):
            print(f"{num}. {options[num-1]}")


    def search_room(player, treasures):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Create a trap dictionary and randomly assign different traps with varying damage values.
        traps = {
            "Snake bite": 4,
            "Posined arrow": 3,
            "Falling rock": 5,
            "Dizziness": 1,
            "Fall from a height": 2
        }
        
        print("\033c", end="")
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        outcome = random.choice(["treasure", "trap"])
        # TODO: Write an if/else to handle treasure vs trap outcomes
        # TODO: Update player dictionary accordingly
        if outcome == 'treasure':
            item = random.choice(list(treasures))
            if item.count("potion") == 1:
                player["health"] += treasures.get(item)
                print(f"\nPlayer found a {item}, health was restored by {treasures.get(item)} points\n")
            else:
                player['inventory'].append(item)
                print(f"\nPlayer found a {item}\n")
        else:
            trap = random.choice(list(traps))
            player['health'] -= traps.get(trap)
            print(f"\nPlayer recieve {trap} damage\n")
        # TODO: Print messages describing what happened


    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        print("\033c", end="")
        # TODO: Print player health
        print(f"\nHealth: {player["health"]}\n")
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”
        if len(player["inventory"]) > 0:
            print(f"Inventory: {', '.join(player["inventory"])}\n")
        else:
            print("You have no items yet.")


    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        print("\033c", end="")
        # TODO: Calculate total score by summing the value of collected treasures
        score = 0
        print("\nCalculating final score...\n")
        for item in player["inventory"]:
            score += treasures.get(item)
        # TODO: Print final health, items, and total value
        # TODO: Implement a scoring system that combines total treasure value and remaining health.
        # Formula used (health * 10) + score.
        score += player["health"] * 10
        print(f"Health: {player["health"]}\nInventory: {', '.join(player["inventory"]) if len(player["inventory"]) > 0 else "You have no items."}\n\nTotal Score: {score}\n")
        # TODO: Allow players to play multiple rounds and track high scores across games.
        
        # TODO: End with a message like "Game Over! Thanks for playing."
        print("\nGame Over! Thanks for playing.\n")

        # TODO: Implement play again feature
        #os.system('cls' if os.name == 'nt' else 'clear')


    def save_scores(player, score):
        """
        Saves score to file for track records of scores.

        Args:
            player(dict): Player stats.
            score(int): Player final score.

        Output:
            Check if file exist for save the score, otherwise create the file and save score.
        """
        print("Saving score...")
        filePath = 'scores.txt'
        if os.path.isfile(filePath):
            print("Scores:\n")
            with open(filePath, 'r') as f:
                print(f)
        else:
            print("File doesn't exist")
            with open("scores.txt", "w") as f:
                f.write(f"{player["name"]}\t\t{score}\t\t{', '.join(player["inventory"]) if len(player["inventory"]) > 0 else "You have no items."}")
                f.close()


    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        for room in range(1,6):
            while player["health"] > 0:
                display_options(room)
        # TODO: Inside each room, prompt player choice using input()
                opt = input("\nSelect your option: ")
        # TODO: Use if/elif to handle each choice (1–4)
        #         match opt:
        #             case "1":
        #                 search_room(player, treasures)
        # # TODO: Break or return appropriately when player quits or dies
        #             case "2":
        #                 break
        #             case "3":
        #                 check_status(player)
        #             case "4":
        #                 print("Thanks for playing.")
        #                 exit()
        #             case _:
        #                 print("\nMust choose a valid option.")
                if opt == "1":
                    search_room(player, treasures)
                elif opt == "2":
                    break
                elif opt == "3":
                    check_status(player)
                elif opt =="4":
                    print("\nThanks for playing.\n")
                    exit()
                else:
                    print("\nMust choose a valid option.")

        if player["health"] < 1:
            print("Player run out of health, Game Over!\n")
        else:
        # TODO: Call end_game() after all rooms are explored
            end_game(player, treasures)


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
