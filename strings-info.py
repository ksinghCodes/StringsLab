message=input(" Enter a message: ")
print(
    ' First charachter:', message[1],
    '\n','Last charachter: ', message[len(message)-1],
    '\n', 'Middle charachter: ', message[int(len(message)/2)],
    '\n', 'Even index charachters: ', message[::2],
    '\n', 'Odd index charachters: ', message[1::2],
    '\n', 'Reveresed message', message[::-1]

)