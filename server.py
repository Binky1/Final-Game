import socket, threading
import time
import tcp_by_size


IP = "0.0.0.0"
PORT = 8001
all_to_die = False

players = 0

socks = []

states = ['idle', 'idle']
ready_players = [False, False]

def handle_client(sock, player):

    ready = tcp_by_size.recv_by_size(sock)
    while ready != 'READY':
        ready = tcp_by_size.recv_by_size(sock)
    ready_players[player] = True
    global players
    players += 1
    print(players)
    i = 1
    while players == 1:
        if i == 1:
            tcp_by_size.send_with_size(sock, 'WAIT')
        i += 1

    tcp_by_size.send_with_size(sock, 'SSTART')

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
                players -= 1
                print('Seems client disconnected')
                break
            elif data == 'GOVER':
                break
            else:
                if data == 'IDLE' or data == 'MOVEFORWD' or data == 'MOVEBACK' or data == 'BLOCK' or data == 'PUNCH':
                    states[player] = data

                    if player == 1:
                        reply = states[0]
                    else:
                        reply = states[1]
                    tcp_by_size.send_with_size(sock, reply)
                else:
                    tcp_by_size.send_with_size(sock, 'SERROR')


            # if player == 1:
            #     states[0] = 'idle'
            # else:
            #     states[1] = 'idle'

            if players == 0:
                finish = True
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
    threads = []

    while True:
        cli_sock, addr = s.accept()
        t = threading.Thread(target=handle_client, args=(cli_sock, currPlayer))
        t.start()
        threads.append(t)
        currPlayer += 1
        # global players
        # players += 1
    for t in threads:
        t.join()
    sys.exit()



if __name__ == '__main__':
    main()