from microbit import *

class sprite():
    def __init__(self, sprite:dict):
        self.sprite = sprite

    def move(self, direction:str, spritePosition, speed:int = 1):
        if (direction.upper() == "UP"):
            for key, value in self.sprite.items():
                updatedValList = []
                for i in range(len(value)):
                    xPos = value[i][0]
                    yPos = value[i][1]
                    coOrdinatePair = [xPos, yPos - speed]
                    updatedValList.append(coOrdinatePair)

                self.sprite[key] = updatedValList
            xPos = spritePosition[0]
            yPos = spritePosition[1]
            spritePosition = [spritePosition[0], spritePosition[1] - speed]

        elif (direction.upper() == "DOWN"):
            for key, value in self.sprite.items():
                updatedValList = []
                for i in range(len(value)):
                    xPos = value[i][0]
                    yPos = value[i][1]
                    coOrdinatePair = [xPos, yPos + speed]
                    updatedValList.append(coOrdinatePair)

                self.sprite[key] = updatedValList
            xPos = spritePosition[0]
            yPos = spritePosition[1]
            spritePosition = [spritePosition[0], spritePosition[1] + speed]

        elif (direction.upper() == "LEFT"):
            for key, value in self.sprite.items():
                updatedValList = []
                for i in range(len(value)):
                    xPos = value[i][0]
                    yPos = value[i][1]
                    coOrdinatePair = [xPos - speed, yPos]
                    updatedValList.append(coOrdinatePair)

                self.sprite[key] = updatedValList
            xPos = spritePosition[0]
            yPos = spritePosition[1]
            spritePosition = [spritePosition[0] - speed, spritePosition[1]]

        elif (direction.upper() == "RIGHT"):
            for key, value in self.sprite.items():
                updatedValList = []
                for i in range(len(value)):
                    xPos = value[i][0]
                    yPos = value[i][1]
                    coOrdinatePair = [xPos + speed, yPos]
                    updatedValList.append(coOrdinatePair)

                self.sprite[key] = updatedValList
            xPos = spritePosition[0]
            yPos = spritePosition[1]
            spritePosition = [spritePosition[0] + speed, spritePosition[1]]

        else:
            print("ERROR")

        return spritePosition

spaceship = { 1: [[0, 3]],
              2: [[1, 2], [1, 3], [1, 4]],
              3: [[2, 2], [2, 3], [2, 4]],
              4: [[3, 1], [3, 2], [3, 3], [3, 4], [3, 5]],
              5: [[4, 1], [4, 5]]
            }
