#This piece of code allows for dynamic, two way communication
#without blocking or taking turns between an Arduino and a computer
#through the use of a visual interface. It works in conjuction with
#a piece of arduino code that must be uploaded to your board.

#This example code is able to turn an LED on and off that is wired to the
#arduino by sending the numbers 1 and 0 respectively. Also wired to
#the arduino is a microswitch. If the microswitch is pressed, the arduino
#sends a number which is displayed on the terminal.

#Both of these processes are fairly basic but they can be replaced with much more
#complex code and more interesting circuits easily. What matters here is the ability
#to send messages back and forth without blocking or a need for python and arduino to
#take turns


#On the formatting of these messages:
#In particular, you can send any message to your arduino board by
#writing it down in a text box and hitting the 'Send Message' button,
#both of which are found on the tkinter interface.
#With that being said, right now it's only programmed to receive numbers
#or single letters.

#The arduino board can send any string which is decoded by the python script.
#This script in particular works on the assumption that the board will only send
#integers and casts those messages as such before using them, but this can be changed.

#I personally find communication through integers easier because you can use a dictionary
#as you would a switch-case statement in c to decode what each integer would represent, as I
#do in this code.

#If you want to send more complex messages like strings, you'll have to do the proper type casting
#on both pieces of code.



#Edgardo Kennedy
#Written on the 4th of january, 2023


import serial #This package allows communication between the arduino and python
import tkinter as tk #We are using tkinter to be able to collect input from the user without blocking



#We initialize the serial port object. Make sure that the port and baudrate values
#align with your arduino and serial port.
ser = serial.Serial(
    port = '/dev/ttyUSB0',\
    baudrate = 9600,\
    parity = serial.PARITY_NONE,\
    stopbits = serial.STOPBITS_ONE,\
    bytesize = serial.EIGHTBITS,\
    timeout = 0
)





#We define and initialize our visual interface object.
master = tk.Tk()

#This adds the label "Message Space" to the interface
tk.Label(master, text = 'Message Space').grid(row = 0, column = 0)

#This adds a text box next to the "Message Space" label
message_space = tk.Entry(master)
message_space.grid(row = 0, column = 1)

#We define two buttons. One to send a message to the arduino
#and another to close the interface.
#The exit button closes the interface window but the code continues to run
#Just use ctrl+c
tk.Button(master,
            text = 'Send Message',
            command = write_to_serial).grid(row = 1, column = 0)
tk.Button(master,
            text = 'Exit',
            command = master.destroy).grid(row = 1, column = 1)





#This function is in charge of sending messages out to the board
def write_to_serial():

    #We retrieve the message written onto the text box
    outgoing_message = message_space.get()
    #We send that message to our arduino
    ser.write(bytes(outgoing_message, 'utf-8'))





def main():

    
    while True:
        #the .in_waiting method returns the number of bytes currently waiting in the buffer.
        #If the value is 0 then the arduino has not sent anything new, if the value is something
        #else then we read the message sent by the arduino.
        while ser.in_waiting:
            #We read and decode the message sent by our board. We assume it's an integer
            incoming_message = int(ser.readline().decode())

            try:
                print(f'Arduino sends the number: {incoming_message}')
            except ValueError:
                print('I had problems reading what the Arduino sent')

        
        master.update_idletasks()
        master.update()


if __name__ == "__main__":
    main()