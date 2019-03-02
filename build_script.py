import subprocess
import os

# # Run the angular application.
# # Angular must be installed.

# Commands.
run_command = "cd client && cd obbclient && ng serve -o"
install_command = "npm install -g angular && cd client && cd obbclient && ng serve -o"


def yes():
    print('Angular will run now')
    client_process = subprocess.Popen(run_command, shell=True)
    client_process.wait()
    print('Press Enter to exit.')
    exit()


def no():
    print('Application will not run.')
    input('Press enter to exit...')
    exit()


def install():
    print("Angular will be installed now.")
    client_process = subprocess.Popen(install_command, shell=True)
    client_process.wait()
    print('Press Enter to exit.')
    exit()


answers = [
    {"Yes": yes},
    {"No. Dont install": no},
    {"No. Install": install},
    {"Exit": exit}
]


def main():
    while True:
        subprocess.call('cls', shell=True)
        print('Is angular installed on your machine?')
        for ans in answers:
            print("[" + str(answers.index(ans)) + "]" + list(ans.keys())[0])
        choice = input(">> ")
        try:
            if int(choice) < 0:
                raise ValueError
            list(answers[int(choice)].values())[0]()
        except(ValueError, IndexError):
            pass


if __name__ == '__main__':
    main()
