import json

class Data():
    def __init__(self):
        #initialize the database from JSON file or create it if it doesn't exist
        self.filename = 'mydatabase.json'
        self.data = self.load_data()

    def load_data(self):
        try:
            #--open the JSON file(read it and save it in the variable "file") and close it after reading it
            with open(self.filename,'r') as file:
                data=json.load(file)
        except FileNotFoundError :
            #--create the JSON file if it doesn't exist
            # { In the game database i have just one table called plyers(it is a list in python),
            # that will contain the name and highscore for each player}
            data = {'players':[]}
        #--return the loaded data
        return data
    
    def save_data(self):
        #--open the JSON file and close it after writtin in it
        with open(self.filename,'w') as file:
            #--write the data  in the file
            json.dump(self.data, file, indent=2)
    
    def add_player(self,player_name,highscore=0):
        
        new_player = {'player_name':player_name, 'highscore':highscore}
        #--add the new player to the players list
        self.data['players'].append(new_player)
        #--save it in the Json file
        self.save_data()

    def edit_highscore(self, player_name,new_highscore):
        for player in self.data['players']:
            if player['player_name'] == player_name:
                player['highscore'] = new_highscore
                self.save_data()
                #player was found and his highscore was successfully modified 
                return True
        #player not found
        return False 
    
    def delete_player(self,player_name):
        for player in self.data['players']:
            if player['player_name'] == player_name:
                #--remove the player from the list
                self.data['players'].remove(player)
                self.save_data()
                return True
            #player not found
        return False
        
    def get_players(self):
        players_data=[]
        for player in  self.data['players']:
            players_data.append((player['player_name'], player['highscore']))
            
        return players_data

    def get_score(self,player_name):
        for player in self.data['players']:
            if player['player_name'] == player_name:
                return player['highscore']
            #player not found
        return False