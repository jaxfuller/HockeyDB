import tkinter as tk
from tkinter import ttk
import sqlite3
import re
from random import randint

class HockeyStats(tk.Tk) :
    def __init__(self):
        super().__init__()
        
        self.title("Hockey Statistics")
        self.geometry("450x600")
        
        #tab control
        self.tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text="Add Game")
        self.tabControl.add(self.tab2, text="Add Team")
        self.tabControl.add(self.tab3, text="View Recent Games")
        self.tabControl.pack(expand=1, fill="both")
        
        #Tab 1MAIN LABEL
        self.titleTab1 = tk.Label(self.tab1, text="Enter Hockey Game Data", font=("Arial", 16), pady=20)
        self.titleTab1.grid(column=0, row=1)
        
        #Date Label
        self.dateLabel = tk.Label(self.tab1, text="Date:", font=("Arial", 12))
        self.dateLabel.grid(column=0, row=2)
        #Date Entry Field
        self.date = tk.StringVar(self.tab1)
        self.dateEntry = tk.Entry(self.tab1)
        self.dateEntry.grid(column=1, row=2, pady=15)

        #Team 1 Name label
        self.team1NameLabel = tk.Label(self.tab1, text="Team 1 Name: (WINNER)", font=("Arial", 14))
        self.team1NameLabel.grid(column=0, row=3)
        #Team 1 Name ENTRY FIELD
        self.mydb = sqlite3.connect("HockeyDB.db")
        self.theCursor = self.mydb.cursor()
        #self.nameQuery = self.theCursor.execute("CREATE TABLE IF NOT EXISTS TEAMS (TEAM_ID PRIMARY KEY AUTOINCREMENT, TEAM_NAME VARCHAR(20), TEAM_LOCATION VARCHAR(20)")
        self.nameQuery = self.theCursor.execute("SELECT TEAM_NAME FROM TEAMS")
        self.nameList = [r for r, in self.nameQuery]
        
        self.team1NameEntry = tk.StringVar(self.tab1)
        self.team1NameEntry.set("Select a team")
        self.dropDown1 = tk.OptionMenu(self.tab1, self.team1NameEntry, *self.nameList)  
        self.dropDown1.grid(column=1, row=3)
        #Team 1 Score Label
        self.team1ScoreLabel= tk.Label(self.tab1, text="Score:", font=("Arial", 12))
        self.team1ScoreLabel.grid(column=0, row=4)
        #Team 1 Score Entry Field
        self.team1Score = tk.StringVar(self.tab1)
        self.team1ScoreEntry = tk.Entry(self.tab1)
        self.team1ScoreEntry.grid(column=1, row=4)
        #Team 1 Shots Label
        self.team1ShotsLabel= tk.Label(self.tab1, text="Shots:", font=("Arial", 12))
        self.team1ShotsLabel.grid(column=0, row=5)
        #Team 1 Shots Entry Field
        self.team1Shots = tk.StringVar(self.tab1)
        self.team1ShotsEntry = tk.Entry(self.tab1)
        self.team1ShotsEntry.grid(column=1, row=5)
        #Team 1 Faceoffs Label
        self.team1FaceoffsLabel= tk.Label(self.tab1, text="Faceoffs:", font=("Arial", 12))
        self.team1FaceoffsLabel.grid(column=0, row=6)
        #Team 1 Faceoffs Entry Field
        self.team1Faceoffs = tk.StringVar(self.tab1)
        self.team1FaceoffsEntry = tk.Entry(self.tab1)
        self.team1FaceoffsEntry.grid(column=1, row=6)
        #Team 1 Penalties Label
        self.team1PenaltiesLabel= tk.Label(self.tab1, text="Penalties:", font=("Arial", 12))
        self.team1PenaltiesLabel.grid(column=0, row=7)
        #Team 1 Penalties Entry Field
        self.team1Penalties = tk.StringVar(self.tab1)
        self.team1PenaltiesEntry = tk.Entry(self.tab1)
        self.team1PenaltiesEntry.grid(column=1, row=7)
        #Team 1 Powerplays Label
        self.team1PowerPlaysLabel= tk.Label(self.tab1, text="Powerplay minutes:", font=("Arial", 12))
        self.team1PowerPlaysLabel.grid(column=0, row=8)
        #Team 1 Powerplays Entry Field
        self.team1PowerPlays = tk.StringVar(self.tab1)
        self.team1PowerPlaysEntry = tk.Entry(self.tab1)
        self.team1PowerPlaysEntry.grid(column=1, row=8)
        
            
        #Team 2 Name Entry label
        self.team2NameLabel = tk.Label(self.tab1, text="Team 2 Name:", font=("Arial", 14))
        self.team2NameLabel.grid(column=0, row=9)
        #Team 2 Name ENTRY FIELD
        self.team2NameEntry = tk.StringVar(self.tab1)
        self.team2NameEntry.set("Select a team")
        
        self.dropDown2 = tk.OptionMenu(self.tab1, self.team2NameEntry, *self.nameList)
        
        self.dropDown2.grid(column=1, row=9)
        #Team 2 Score Label
        self.team2ScoreLabel= tk.Label(self.tab1, text="Score:", font=("Arial", 12))
        self.team2ScoreLabel.grid(column=0, row=10)
        #Team 2 Score Entry Field
        self.team2Score = tk.StringVar(self.tab1)
        self.team2ScoreEntry = tk.Entry(self.tab1)
        self.team2ScoreEntry.grid(column=1, row=10)
        #Team 2 Shots Label
        self.team2ShotsLabel= tk.Label(self.tab1, text="Shots:", font=("Arial", 12))
        self.team2ShotsLabel.grid(column=0, row=11)
        #Team 2 Shots Entry Field
        self.team2Shots = tk.StringVar(self.tab1)
        self.team2ShotsEntry = tk.Entry(self.tab1)
        self.team2ShotsEntry.grid(column=1, row=11)
        #Team 2 Faceoffs Label
        self.team2FaceoffsLabel= tk.Label(self.tab1, text="Faceoffs:", font=("Arial", 12))
        self.team2FaceoffsLabel.grid(column=0, row=12)
        #Team 2 Faceoffs Entry Field
        self.team2Faceoffs = tk.StringVar(self.tab1)
        self.team2FaceoffsEntry = tk.Entry(self.tab1)
        self.team2FaceoffsEntry.grid(column=1, row=12)
        #Team 2 Penalties Label
        self.team2PenaltiesLabel= tk.Label(self.tab1, text="Penalties:", font=("Arial", 12))
        self.team2PenaltiesLabel.grid(column=0, row=13)
        #Team 2 Penalties Entry Field
        self.team2Penalties = tk.StringVar(self.tab1)
        self.team2PenaltiesEntry = tk.Entry(self.tab1)
        self.team2PenaltiesEntry.grid(column=1, row=13)
        #Team 2 Powerplays Label
        self.team2PowerPlaysLabel= tk.Label(self.tab1, text="Powerplay minutes:", font=("Arial", 12))
        self.team2PowerPlaysLabel.grid(column=0, row=14)
        #Team 2 Powerplays Entry Field
        self.team2PowerPlays = tk.StringVar(self.tab1)
        self.team2PowerPlaysEntry = tk.Entry(self.tab1)
        self.team2PowerPlaysEntry.grid(column=1, row=14)
        
        #Submit Game BUTTON
        self.submitGameButton = tk.Button(self.tab1, text="Submit", fg="white", bg="blue", pady=15, command=self.AddGame)
        self.submitGameButton.grid(column=0, row=15)
        #Clear Game Button
        self.clearButton = tk.Button(self.tab1, text="Clear Data", fg="white", bg="blue", pady=15, command=self.clearGame)
        self.clearButton.grid(column=1, row=15)
        #Quit Button
        self.QuitButton = tk.Button(self.tab1, text="Exit", fg="white", bg="blue", pady=10, command=quit)
        self.QuitButton.grid(column=1, row=1)
        
        
        
        #Tab 2 MAIN LABEL
        self.titleTab2 = tk.Label(self.tab2, text="Enter a New Team", font=("Arial", 16), pady=20)
        self.titleTab2.grid(column=0, row=0)
        #New Team Name Label
        self.newTeamNameLabel = tk.Label(self.tab2, text="New Team Name:", font=("Arial", 12))
        self.newTeamNameLabel.grid(column=0, row=2)
        #New Team Name Entry
        self.newTeamName = tk.StringVar(self.tab2)
        self.newTeamNameEntry = tk.Entry(self.tab2)
        self.newTeamNameEntry.grid(column=1, row=2)
        #New Team Location Label
        self.newTeamLocationLabel = tk.Label(self.tab2, text="New Team City:", font=("Arial", 12))
        self.newTeamLocationLabel.grid(column=0, row=3)
        #NewTeam Location Entry
        self.newTeamLocation = tk.StringVar(self.tab2)
        self.newTeamLocationEntry = tk.Entry(self.tab2)
        self.newTeamLocationEntry.grid(column=1, row=3)
        
        
        #Submit New Team Button
        self.newTeamSubmit = tk.Button(self.tab2, text="Submit", fg="white", bg="blue", pady=15, command=self.AddTeam)
        self.newTeamSubmit.grid(column=0, row=4)
        #Clear Data New Team Button
        self.newTeamClear = tk.Button(self.tab2, text="Clear", fg="white", bg="blue", pady=15)
        self.newTeamClear.grid(column=1, row=4)
        
        #tab3
        #Recent Games lable
        self.recentGamesLabel = tk.Label(self.tab3, text= "Recent Games", font=("Arial", 16))
        self.recentGamesLabel.grid(column=0, row=0)
        
        self.recentDateLabel = tk.Label(self.tab3, text="Date", font=("Arial", 12))
        self.recentDateLabel.grid(column=0,row=1)
        
        self.winnerLabel = tk.Label(self.tab3, text="Winner", font=("Arial", 12))
        self.winnerLabel.grid(column=1, row=1)
        
        self.winnerScoreLabel = tk.Label(self.tab3, text="Score", font=("Arial", 12))
        self.winnerScoreLabel.grid(column=2, row=1)
        
        self.loserLabel = tk.Label(self.tab3, text="Opponent", font=("Arial", 12))
        self.loserLabel.grid(column=3, row=1)   
        
        self.loserScoreLabel = tk.Label(self.tab3, text="Score", font=("Arial", 12))
        self.loserScoreLabel.grid(column=4, row=1) 
        
        #Recent games table
        self.mydb = sqlite3.connect('HockeyDB.db')
        self.Cursor3 = self.mydb.cursor()
        self.recentGames = self.Cursor3.execute("SELECT * FROM [Recent_Games] ORDER BY DATE DESC")
        i = 0
        for game in self.recentGames:
            for j in range(len(game)):
                self.e = tk.Entry(self.tab3, width=10)
                self.e.grid(row=i+2, column=j)
                self.e.insert(tk.END, game[j])
            i = i+1
        self.Cursor3.close()    
        
    def AddGame(self):
        date = str(self.dateEntry.get())
        team1Name = str(self.team1NameEntry.get())
        team1Score = int(self.team1ScoreEntry.get())
        team1Shots = int(self.team1ShotsEntry.get())
        team1Faceoffs = int(self.team1FaceoffsEntry.get())
        team1Penalties = int(self.team1PenaltiesEntry.get())
        team1PowerPlays = int(self.team1PowerPlaysEntry.get())
        team2Name = str(self.team2NameEntry.get())
        team2Score = int(self.team2ScoreEntry.get())
        team2Shots = int(self.team2ShotsEntry.get())
        team2Faceoffs = int(self.team2FaceoffsEntry.get())
        team2Penalties = int(self.team2PenaltiesEntry.get())
        team2PowerPlays = int(self.team2PowerPlaysEntry.get())
        
        gameID = str(re.sub(r"[-/]","", date)+ "-" + str(randint(0,1000)))

        
        mydb = sqlite3.connect('HockeyDB.db')
        theCursor = mydb.cursor()
        theCursor.execute("INSERT INTO GAMES (GAME_ID, DATE, TEAM1_NAME_WINNER, TEAM1_SCORE, TEAM1_SHOTS, TEAM1_FACEOFFS, TEAM1_PENALTIES, TEAM1_POWERPLAYS, TEAM2_NAME, TEAM2_SCORE, TEAM2_SHOTS, TEAM2_FACEOFFS, TEAM2_PENALTIES, TEAM2_POWERPLAYS) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (gameID, date, team1Name, team1Score, team1Shots, team1Faceoffs, team1Penalties, team1PowerPlays, team2Name, team2Score, team2Shots, team2Faceoffs, team2Penalties, team2PowerPlays))
        mydb.commit()
        mydb.close()
        
    def AddTeam(self):
        newTeamName = str(self.newTeamNameEntry.get())
        newTeamLocation = str(self.newTeamLocationEntry.get())
        
        mydb = sqlite3.connect('HockeyDB.db')
        theCursor = mydb.cursor()
        theCursor.execute("INSERT INTO TEAMS (TEAM_NAME, TEAM_LOCATION) VALUES (?,?)", (newTeamName, newTeamLocation))
        mydb.commit()
        mydb.close()
        
    def clearGame(self):
        self.dateEntry.delete(first=0, last=10)
        self.team1NameEntry.set("Select a team")
        self.team1ScoreEntry.delete(first=0, last=2)
        self.team1ShotsEntry.delete(first=0, last=2)
        self.team1FaceoffsEntry.delete(first=0, last=2)
        self.team1PenaltiesEntry.delete(first=0, last=2)
        self.team1PowerPlaysEntry.delete(first=0, last=2)
        self.team2NameEntry.set("Select a team")
        self.team2ScoreEntry.delete(first=0, last=2)
        self.team2ShotsEntry.delete(first=0, last=2)
        self.team2FaceoffsEntry.delete(first=0, last=2)
        self.team2PenaltiesEntry.delete(first=0, last=2)
        self.team2PowerPlaysEntry.delete(first=0, last=2)
    
    def quit(self):
        self.destroy()
        
def main():
    window = HockeyStats()
    HockeyStats.mainloop(window)
    
while __name__ == "__main__":
    main()