# AR-Sudoku-Solver
![](https://img.shields.io/badge/python-3.8-blue)
![](https://img.shields.io/badge/contributers-1-green)
![](https://img.shields.io/badge/license-MIT-lightgrey)

A augmented reality sudoku solver using random forest classifier and backtracking algorithm

Link to demo -> [demo](https://www.linkedin.com/posts/yash-indane-aa6534179_python3-opencv-machinelearning-activity-6689535809860730880-TBgS)

![sudoku-g](https://user-images.githubusercontent.com/53041219/207026036-817b50d8-3f09-4e2a-b145-5b721f64e60c.gif)

## Description
1.Building the dataset

For building the dataset the same program is used which is used for capturing the square grids during solving.

Installation

`$ pip install opencv-python`

By this method we are capturing 23 by 23 size grayscale images. There are 529 features, upon which the classifier will be trained.

Sample training images - ![12](https://user-images.githubusercontent.com/53041219/207026383-9083db7a-7673-4b8a-bba9-24e3af09745d.png) ![11](https://user-images.githubusercontent.com/53041219/207026476-3229c982-9364-4524-a10b-bd0a6d07e501.png) ![8](https://user-images.githubusercontent.com/53041219/207026526-f8e8b479-0d78-484d-9384-21b22920dd9a.png)

Total 1600 images of numbers from 0-9 are then fed to the dataset generator program which generates the required `.csv` file. The generated file
with 530 coloumns is then used by model builder , which makes a random forest classifier. Accurracy acheived on test data is around 98%.

### What is Random Forest Classification?

![a](https://user-images.githubusercontent.com/53041219/207026638-d6ccda3d-cb25-4d4e-af95-0d12f5557f48.png) ![forest2](https://user-images.githubusercontent.com/53041219/207026711-dfd6de2a-3a9b-4722-afac-2c69a4e96da7.png)

A Random Forest Classifier is a set of decision trees which randomly select subset of training set. The final decision comes from the aggregation of votes 
from all the trees. It has been implemented with the scikit-learn library. 

### Note-
(optional) For shuffling up the csv file we can do this after reading the file- 

```py
data = data.sample(frac=1).reset_index(drop=True)
```

## Grabbing the digits from the grid

Countours are been used to detect polygons present in the live video. They later are been filtered out on the basis of countour-area and no. of sides.

![detection1](https://user-images.githubusercontent.com/53041219/207026797-dfcc804e-6357-4b17-b5b5-a0c7c24d2c83.png)

The extracted digits are then predicted using our pre-trained ML model , and the whole numbers are sent to the sudoku solver which solves it with efficient backtracking
algorithm.

## Solving 

Backtracking algorithm - Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.

![ss1](https://user-images.githubusercontent.com/53041219/207026872-604ecb90-a756-4f3d-a677-c0cc01444a48.png)

One of the fastest solves in 16 msecs!

![fastest_solve](https://user-images.githubusercontent.com/53041219/207026926-3770756d-a01e-4c5a-b1ff-d6e8e98f8cf8.png)

## Sudoku Solving Vizualizer

![](sudoku.gif)

## Resources
For getting the sudoku puzzles go to  - http://www.websudoku.com/

For getting solution of puzzles go to - https://sudokusolver.net/
