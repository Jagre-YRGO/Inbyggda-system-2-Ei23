#include <SPI.h>

#define CAN_2515

// For Arduino MCP2515 Hat:
// the cs pin of the version after v1.1 is default to D9
// v0.9b and v1.0 is default D10
const int SPI_CS_PIN = 9;
const int CAN_INT_PIN = 2;

#ifdef CAN_2515
#include "mcp2515_can.      h"
mcp2515_can CAN(SPI_CS_PIN); // Set CS pin
#endif

const int LED_ON  = 1;
const int LED_OFF = 0;
const int buttonPin = 8; // Define the pin number you want to read
const int LEDPin = 5; // Define the pin number you want to read
const int LEDPin_recv = 6;
unsigned char flagRecv = 0;

void MCP2515_ISR() {
    flagRecv = 1;
}

void setup() {
    pinMode(LEDPin, OUTPUT); // Set the LED pin as an output
    pinMode(6, OUTPUT); // Set the LED pin as an output
    digitalWrite(LEDPin, LOW);
    digitalWrite(6, LOW);
    
    SERIAL_PORT_MONITOR.begin(115200);
    while (!SERIAL_PORT_MONITOR) {}



    while (CAN_OK != CAN.begin(CAN_500KBPS)) {             // init can bus : baudrate = 500k
        SERIAL_PORT_MONITOR.println("CAN init fail, retry...");
        delay(100);
    }
    SERIAL_PORT_MONITOR.println("CAN sender init ok!");
}

unsigned char buf_new, buf_old;
int buttonState = 0;
unsigned char len = 0;
unsigned char buf[8];

void loop() {
    buf_new = (unsigned char)digitalRead(buttonPin);

    if (buf_new != buf_old){
      if (buf_new == 1) {
        //SERIAL_PORT_MONITOR.println("pressed!");
        digitalWrite(LEDPin, HIGH);
      } else {
        //SERIAL_PORT_MONITOR.println("released!");
        digitalWrite(LEDPin, LOW);
      }
    }
  
    CAN.sendMsgBuf(0x0A, 0, 1, &buf_new);
    delay(100);                       // send data 10 times per second
    buf_old = buf_new;

    while (CAN_MSGAVAIL == CAN.checkReceive()) {
        // read data,  len: data length, buf: data buf
        CAN.readMsgBuf(&len, buf);

        if (buf[0] == 0){
          digitalWrite(LEDPin_recv, LOW);
        } else {
          digitalWrite(LEDPin_recv, HIGH);
        }
    }
}

/*********************************************************************************************************
    END FILE
*********************************************************************************************************/
