class Player:
  def play(self):
      print("The Player Is Playing Cricket. ")

class Batsman(Player):
  def play(self):
    print("The Batsman is Batting.")

class Bowler(Player):
  def play(self):
    print("The bowler is Bowling.")

batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()
