started = False

while True:
    check_text = input('>').lower()
    if check_text == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')

    elif check_text == 'start':
        if started:
            print('Car is already started.')
        else:
            started = True
            print('Car started... Ready to go!')
    elif check_text == 'stop':
        if not started:
            print('Car is already stopped.')
        else:
            started = False
            print('Car stopped')

    elif check_text == 'quit':
        break

    else:
        print("I don't understand that...")
