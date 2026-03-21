import random, os

FILE_PATH = "scores.txt"

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
        ##print("\033c", end="")
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
            inventory = shrink_inventory(player["inventory"])
            [print(f"Inventory: {k} x{inventory.get(k)}", end=', ') for k in inventory.keys()]
        else:
            print("You have no items yet.")

    def shrink_inventory(inv: list) -> dict:
        """
        Shrinks the inventory to unique object collected and display the amounts

        Args:
            inv (list): List containing the actual inventory of the player.

        Return:
            dict: Example:
                {
                "['amethyst']": 5, 
                "['gold ring']": 2, 
                "['shiny garnet']": 3, 
                "['diamond']": 1, 
                "['dusty map']": 1
                }
        """
        unique = []
        counter = []
        # List comprehension for unique items
        [unique.append(a) for a in inv if a not in unique]
        # List comprehension for count the unique items
        [counter.append(inv.count(c)) for c in unique]
        # Dict containing the unique items and their respective amount
        inventory = {str(unique[i]): counter[i] for i in range(len(unique))}
        return inventory


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
        print(f"\t\tHealth: {player["health"]}\n\t\tInventory: {', '.join(player["inventory"]) if len(player["inventory"]) > 0 else "\t\tYou have no items."}\n\n\t\tTotal Score: {score}\n")
        # TODO: Allow players to play multiple rounds and track high scores across games.
        save_scores(player, score)
        # TODO: End with a message like "Game Over! Thanks for playing."
        print("\nGame Over! Thanks for playing.\n")
        print("High Scores of Dungeon Adventure:\n")
        show_scores()
        # TODO: Implement play again feature
        retry = False
        while retry == False:
            choice = input("\nDo you wish to try another run? y/n.\n")
            if choice == "n":
                exit()
            elif choice == "y":
                print("\033c", end="")
                main()
            else:
                print("\033c", end="")
                print("\nInvalid input\n")


    def save_scores(player: dict, score: int):
        """
        Saves score to file for track records of scores.

        Args:
            player(dict): Player stats.
            score(int): Player final score.

        Output:
            Save obtain score to file.
        """
        print("Saving score...")
        data = f"{player["name"]}+{score}+{', '.join(player["inventory"]) if len(player["inventory"]) > 0 else "You have no items."}\n"
        write_file(data)

        
    def write_file(data: str):
        """
        Method for file creation and modification.

        Args:
            data (str): Player data to append
        """
        with open(FILE_PATH, "a") as fp:
            fp.write(data)
            fp.close()


    def read_scores()-> list:
        """
        Method for read the file and obtain all lines of the players scores.

        Returns:
            list: Example:
                [
                    ['Someone','34','dusty map'],
                    ['Another','56','diamond, ruby, amethyst']
                ]

        """
        lines = []
        if os.path.isfile(FILE_PATH):
            with open(FILE_PATH, "r") as fp:
                content = fp.readlines()
                for line in content:
                    lines.append(line.strip())
                fp.close()
        return lines


    def show_scores():
        """
        Prints scores recorded in the game.

        Output:
            Shows top 4 scores in descending order.
            Example:
                100 - Someone
                59 - Another
                1 - Maybe
        """
        # Call the method to read the file containing the scores
        lines = read_scores()
        cured_lines = []
        # Parsing data using separator '+' to divide player name, score, inventoryy
        for p in lines:
            cured_lines.append(p.split("+")[:2])
        # Sorting using lambda function to organize the list from low to high
        ord = sorted(cured_lines, key=lambda a:int(a[1]))
        # Reversing the list to get the top scores first
        tst = [score for score in ord[::-1]]
        # Printing top four scores in the list
        if len(tst) < 5:
            [print(' - '.join(top)) for top in tst]
        else:
            for top in range(5):
                print(' - '.join(tst[top][::-1]))


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
                    print("\033c", end="")
                    break
                elif opt == "3":
                    check_status(player)
                elif opt =="4":
                    print("\nThanks for playing.\n")
                    exit()
                else:
                    print("\033c", end="")
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
