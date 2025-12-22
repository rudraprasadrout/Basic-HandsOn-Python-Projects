#  Who wants to be a millionier game using python 

questions = [
    ["What is the capital of France?", "A. Paris", "B. Berlin", "C. Rome", "D. Madrid", 1],
    ["Which planet is known as the Red Planet?", "A. Earth", "B. Mars", "C. Jupiter", "D. Venus", 2],
    ["Who wrote 'Romeo and Juliet'?", "A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain", 1],
    ["What is the largest mammal in the world?", "A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark", 2],
    ["Which element has the chemical symbol 'O'?", "A. Gold", "B. Oxygen", "C. Silver", "D. Iron", 2],
    ["In which year did the Titanic sink?", "A. 1912", "B. 1905", "C. 1920", "D. 1898", 1],
    ["What is the square root of 64?", "A. 6", "B. 7", "C. 8", "D. 9", 3],
    ["Who painted the Mona Lisa?", "A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo", 3],
    ["What is the smallest prime number?", "A. 0", "B. 1", "C. 2", "D. 3", 3],
    ["Which gas do humans primarily exhale?", "A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen", 2],
    ["Which continent is the Sahara Desert located in?", "A. Asia", "B. Africa", "C. Australia", "D. South America", 2]
]

prizes = [100,150,200,250,300,350,400,450,500,550,600]
i = 0 

for question in questions:
    print(question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4])

    # check the answer is correct or not 
    a = int(input("Enter your answer:  1 for a , 2 for b , 3 for c , 4 for d  "))
    if(question[5] == a):
        print("Hurray ! Correct answer")
    else:
        print(f"Oops Incorrect , the correct answer was {question[5]}")
        print("Better Luck Next Time!!")
        break
    print(f"You Won {prizes[i]} $")
    i += 1

