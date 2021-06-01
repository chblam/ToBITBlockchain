from blockchain import Blockchain

if __name__ == '__main__':
    try:
        difficulty = int(input("Please specify the difficulty: "))
    except:
        print("Invalid input!")

    print("Creating Genesis Block...")
    testchain = Blockchain(difficulty)
    print("Genesis Block created")

    while (True):
        data = input("Please enter your message: ") + " from "
        data += input("Please enter your name: ") + " to "
        data += input("Please enter the recipient's name: ")
        testchain.add_to_mempool(data)
        testchain.mine()

