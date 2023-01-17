//This works in conjunction with a piece of python code. It allows for
//dynamic, two way communication between your arduino and your computer
//without blocking and without the need for them to take turns.

//Currently, all the arduino does is read if a microswitch is being pressed
//and turn an LED on and off. If the microswitch is pressed then it sends
//a message to the computer, and it turns the LED on and off depending if the
//computer tells it to.

//More complex things can be done with this code, of course. This just provides
//a framework for the communication.

//Things to note: 
//*The microswitch is finicky, I didn't spend much time dealing with rebouncing
//*The do-while(Serial.available()==0) is crucial, it's what allows the arduino
// to take messages from the pc dynamically.

//Edgardo Kennedy
//Written on the 4th of january, 2023


//We define the pins for our microswitch and our LED
const int Button_Pin = 2;
const int LED_Pin = 5;


void setup() {
  //You need Serial.begin() here. The baudrate must match what it says on the python script.
  Serial.begin(9600);

  //Typical pinMode for our switch and LED
  pinMode(Button_Pin, INPUT);
  pinMode(LED_Pin, OUTPUT);
}



void loop() {

  //A variable for storing what the computer is sending. It's defined as an integer but really,
  //it's expecting a byte that can be any char, so any digit or a letter.
  //It's initialized as a -1 but it can be anything. Just make sure whatever you initialize it to
  //doesn't match anything that the computer could be sending. This way the arduino won't misinterpret it
  //for something else
  int Incoming_Order = -1;

  //If Serial.available() returns anything but a zero, that means there's something waiting to be
  //received from the computer
  if(Serial.available() > 0) {
    Incoming_Order = Serial.read();
  }

  //We interpret what the message from the computer means. This message will regularly be an instruction
  //from the computer. Currently, if we received the char '0' then we turn the LED off. If we received the
  //char '1', then we turn the LED on.
  //If you have more than two possibilities, a switch-case statement might be better
  if(Incoming_Order == '0'){
    digitalWrite(LED_Pin, LOW);
  }else if(Incoming_Order == '1'){
    digitalWrite(LED_Pin, HIGH);
  }

  //We run the function to check if the microswitch is pressed.
  //This do-while needs to be here. What it does is run whatever code
  //the arduino is meant to execute as long as there's no message from the computer
  //waiting to be received by the arduino. If there is a message, the arduino leaves
  //this loop to retrieve the message at the top of this void loop() function. Once
  //the message has been received, the arduino does whatever it needs to do with it
  //and then goes back to this
  do{
    Button_Function();
  }while(Serial.available() == 0);
  

}


//This function is in charge of checking if the microswitch is being pressed
//If it is, then the arduino sends a message to the computer. In this case the message
//is the counter variable, which is just an integer that goes up by one everytime the 
//switch is pressed. 
void Button_Function(){

  //We have two microswitch variables here to deal with rebouncing but it's not the best solution
  static int microswitch_1 = 0;
  static int microswitch_2 = 0;
  static int counter = 0;
  
  microswitch_1 = digitalRead(Button_Pin);
  if(microswitch_1){
    microswitch_2 = 1;
  }
  while(microswitch_1){
    microswitch_1 = digitalRead(Button_Pin);
  }
  if(microswitch_2){
    microswitch_2 = 0;
    Serial.println(counter);
    counter++;
  }
      


  
}
