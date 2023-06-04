import socket, threading
import time
import tcp_by_size


IP = "0.0.0.0"
PORT = 8001
all_to_die = False

players = 0

socks = []

states = ['idle', 'idle']

def handle_client(sock, player):

    ready = tcp_by_size.recv_by_size(sock)
    while ready != 'RADY':
        ready = tcp_by_size.recv_by_size(sock)

    global players
    players += 1
    print(players)
    i = 1
    while players == 1:
        print('Waiting')
        if i == 1:
            tcp_by_size.send_with_size(sock, 'WAIT')
        i += 1

    tcp_by_size.send_with_size(sock, 'STRT')

    global all_to_die

    finish = False
    print(f'New Client number')

    socks.append(sock)


    while not finish:
        if all_to_die:
            print('will close due to main server issue')
            break
        try:
            

            data = tcp_by_size.recv_by_size(sock)  # todo improve it to recv by message size
            print(str(player) + ' ' + data)
            if data == '':
                print('Seems client disconnected')
                break
            else:
                if data == 'NGME':
                    states[player] = 'idle'
                else:
                    states[player] = data

            if player == 1:
                reply = states[0]
            else:
                reply = states[1]
            tcp_by_size.send_with_size(sock, reply)

            # if player == 1:
            #     states[0] = 'idle'
            # else:
            #     states[1] = 'idle'


            if finish:
                time.sleep(1)
                break
        except socket.error as err:
            print(f'Socket Error exit client loop: err:  {err}')
            break
        except Exception as err:
            print(f'General Error %s exit client loop: {err}')
            break
    sock.close()


def main():

    s = socket.socket()
    s.bind((IP, PORT))
    s.listen(2)

    currPlayer = 0
    
    while True:
        cli_sock, addr = s.accept()
        t = threading.Thread(target=handle_client, args=(cli_sock, currPlayer))
        t.start()
        currPlayer += 1
        # global players
        # players += 1


if __name__ == '__main__':
    main()