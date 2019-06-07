class AccountAccessSecurityStrategy:
  def getStrategy(int):
    pass

class Level0AccountAccess:
  def viewAccount():
    pass
  def modifyAccount():
    pass
    
class Level2AccountAccess:
  def viewAccount():
    pass
  def modifyAccount():
    pass
  def deleteAccount():
    pass

"""
AccountAccessStrategy
Level0AccountAccess and Level2AccountAccess both inherit from AccountAccess

"""
