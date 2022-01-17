
import socket
import ssl
import json


def xtb(ID, password):

    host = 'xapi.xtb.com'
    port_main = 5112
    streaming_port = 5113

    USERID = ID

    PASSWORD = password

    answer = True

    while answer:

        try:

            host = socket.getaddrinfo(host, port_main)[0][4][0]

            s = socket.socket()
            s.connect((host, port_main))
            s = ssl.wrap_socket(s)

            parameters = {
                "command" : "login",
                "arguments" : {
                    "userId": USERID,
                    "password": PASSWORD

                }
            }
            packet = json.dumps(parameters, indent=4)
            s.send(packet.encode("UTF-8"))

            END = b'\n\n'
            response = s.recv(8192)

            if END in response:
               "print('Print login: {}'.format(response[:response.find(END)]))"

            '#print(type(response))'
            '#print(response)'

            odp = response.decode("UTF-8")
            odp_dic = json.loads(odp)

            stream_Id = odp_dic['streamSessionId']
            '#print(stream_Id)'

            balances = {

                "command": "getBalance",
                "streamSessionId": stream_Id

            }

            host_str = socket.getaddrinfo(host, streaming_port)[0][4][0]
            s2 = socket.socket()
            s2.connect((host_str, streaming_port))
            s2 = ssl.wrap_socket(s2)
            s2.settimeout(5)
            paczka = json.dumps(balances)
            s2.send(paczka.encode("UTF-8"))
            responses = s2.recv(8192)

            if responses != 0:

                answer = False

        except:
            '#print ("Coś poszło nie tak, spróbujmy jeszcze raz")'
            answer = True

    '#print(f"odpowiedz balaces: {responses}")'
    profit = responses.decode("UTF-8")
    profit_dic = json.loads(profit)
    profits = profit_dic['data']
    #print(profits['equity'])

    parameters = {
        "command": "logout"
    }

    packet = json.dumps(parameters, indent=4)
    s.send(packet.encode("UTF-8"))

    response = s.recv(8192)

    if END in response:
        """print('Print logout: {}'.format(response[:response.find(END)]))"""

        return profits['equity']


