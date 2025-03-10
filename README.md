# Web Application Platform for Behavioral Experiments In Non-human Primates

### An improvement to Marmoset Experimental Behavioral Instrument (MXBI) Platform

## Behavioral and Cognitive Neuroscience Lab : Faculty of Medicine at Chulalongkorn University

This project aims to replicate and enhance the work conducted by A. Calapai et al. (2022).

[Flexible auditory training, psychophysics, and enrichment of common marmosets with an automated, touchscreen-based system (A. Calapai, J. Cabrera-Moreno, T. Moser & M. Jeschke)](https://www.nature.com/articles/s41467-022-29185-9)

### Full documentation avialable at 
https://beacon-lab-med-chula.github.io/PrimatesBehaviorWebApp/


## Overview

<img src="./img/device1.png" alt="device" width="400"/>


A modular, cage-based device designed for adaptability in various experiments focused on computer-based cognitive training and audio-visual association studies, to facilitate the investigation of non-human primates' behavioral traits and complex nervous systems.

Contribute to the development and optimization of cognitive and environmental enrichment strategies for non-human primates under human care.

Incorporated a web application platform for remote access and control, providing rapid prototyping speed and convenience for researchers.

### Key Features

- A cage-based device built on the Raspberry Pi platform.
- 3-tier architecture,  client / application server / database server.
- RESTful API.
- Animal tagging by means of radio-frequency identification 
- Capable of experiment on cognitive vision / auditory tasks
- Scalable to multiple instruments
- An open-architecture, scalable, and customizable experiment platform (Django, JavaScript).
- User authentication and authorization for enhanced security and management.
- Dynamic content updates allow users to observe each experiment's status in real time.


## Apparatus (Prototype)

A cage-based device is designed according to the marmoset experimental behavioral instrument (MXBI) [A.Calapai et al. 2022]. The device's design has been slightly modified from MXBI to enhance the capabilities of experiments. 

The main component is divided into three sections.
- Behavioral chamber
- Electronic compartment 
- Waste bin

### Integrated System Implementation.

This section provides details about the system's hardware in the electronic compartment and touchscreen section.

#### Equipments

The electronics compartment on the ​left side of the instrument contains:

- Raspberry Pi 4 Model B
- Raspberry Pi Camera Module 3
- 2x Visaton FR58, 8 Ω, 120–20,000 Hz: Note that one speaker is housed in the electronics compartment, while the other is wired to the opposite side of the instrument.
- Peristaltic pump (JIHPUMP MN3 Mini OEM Peristaltic Pumps MN3/BT)
- 134.2K WL-134 Long distance RFID Animal Tag Reader Module
- 24v 7Ah Lithium ion battery with XT60 connector
- HW-652 YAMAHA YDA138-E 12W+12W Dual Channel Digital Audio Amplifier Board DC 12V 
- TB6600 Single Axis 4A Stepper Motor Driver Controller 9~42V Micro-Step CNC
- 3x 300W 20A DC-DC Adjustable Step Down Converter Module Constant Current

The behavioral chamber in the middle hosts:

- Waveshare 10.1inch Resistive Touch Screen LCD

#### Schematic Diagram

<img src="./img/schematic_diagram.png" alt="schematic_diagram" />

The system utilizes a Raspberry Pi single-board computer to provide general-purpose input/output (GPIO) capabilities, enabling researchers to interface with a diverse range of external hardware components. The modular design allows for flexible hardware configurations tailored to specific task requirements. 

#### Touch Screen Connection

A 10-inch Waveshare HDMI LCD touchscreen is employed for visual cognition tasks. To facilitate resistive touch functionality, only five pins are necessary for communication via the Serial Peripheral Interface (SPI) protocol.

1. SCK (Serial Clock): Clock signal from the master (Raspberry Pi) to synchronize data transmission.
2. MOSI (Master Out Slave In): Used for sending data from the master (Raspberry Pi) to the touchscreen controller.
3. MISO (Master In Slave Out): Used for receiving data from the touchscreen controller to the master.
4. CE1 (Chip Enable 1/Chip Select 1): Used to select the touchscreen for communication (low active).
5. IRQ (Interrupt Request): Used by the touchscreen to signal the master that an event has occurred (low level while the Touch Panel detects touching).

To preserve the remaining GPIO pins and ensure a modular design, the Raspberry Pi is not mounted directly onto the display module, as recommended in Waveshare’s documentation. Instead of soldering the five pins directly from the back of the panel to connect to the Raspberry Pi, a detachable interface is utilized. Refer to the diagram below for the connection details.

<img src="./img/touchscreen_diagram.png" alt="touchscreen_diagram"/>

The panel requires screen configuration and touch calibration before it can be operational. Refer to the 'Software Setting' and 'Touch Calibration' sections in the Waveshare documentation for detailed instructions.

[Waveshare 10.1inch HDMI LCD Documentation](https://www.waveshare.com/wiki/10.1inch_HDMI_LCD)

#### Peristaltic Pumps Connection

<img src="./img/pump.png" alt="pump" width="200"/>

The Mini OEM Peristaltic Pump, model MN3/BT from JIHPump, is powered by a 24V DC, 48W stepper motor. To unlock its full potential, the system utilizes a TB6600 controller, enabling precise control and synchronization.

The MN3/BT employs a 4-wire stepper motor, comprising two coils, with each coil featuring two wires. The wiring configuration is illustrated in the diagram below.

If a different stepper motor is used, identify the wires belonging to the same coil by measuring the resistance between them using a multimeter.
- If two wires are part of the same coil, they will show a measurable resistance (typically a few ohms).
- If the wires are from different coils, the resistance will be very high (open circuit).

To control the motor, three pins are required.
- PUL (Pulse): This pin is used to control the steps of the stepper motor. Each pulse sent to this pin will cause the motor to move one step. The frequency of the pulses determines the speed of the motor.

- DIR (Direction): This pin controls the direction of the motor rotation. A high signal (5V) will make the motor rotate in one direction, and a low signal (0V) will make it rotate in the opposite direction.

- ENA (Enable): This pin is used to enable or disable the motor. When this pin is high, the motor is disabled, and when it is low, the motor is enabled.

PUL, DIR, and ENA are connected to the microcontroller’s digital output pins.

<img src="./img/motor_diagram.png" alt="motor_diagram" width="400"/>

Additionally, the TB6600 stepper motor driver features six DIP (Dual In-line Package) switches on its board. These switches are used to configure two key parameters:

- Current: This sets the maximum current that the driver will supply to the motor. The configured current must not exceed the motor's rated current capacity.

- Microstep: Microstepping enables finer control of the stepper motor, resulting in smoother rotation and improved precision."

The switches on the DIP switch bar are binary, with only two possible positions: on (1) and off (0).

<img src="./img/dip.png" alt="dip" width="400"/>

Refer to the diagram below for the switch numbering and their corresponding configurations.

<img src="./img/dip_diagram.png" alt="dip_diagram" />

The stepper motor's current (amp) setting can be found in the model's specification sheet. For the MN3/BT stepper motor used in this project, a current setting of 2 amps is required, corresponding to the switch configuration S4, S5, S6 as ON, OFF, OFF.

Reference : [How to set dip switches correctly](https://drufelcnc.com/?c=blog&p=DipSwitches)


## Web Application

Delivering diverse tasks to analyze the phenotypic characteristics of non-human primates, as well as their complex nervous systems, necessitates distinct configurations of both hardware and software, each tailored to the specific requirements of the task.

For this reason, combined with the flexibility of the GPIO on the Raspberry Pi system, which enables reconfigurable peripherals, we have designed the web application system with the idea of modularity to allow scalability of the experiments.

The idea is to use the Django framework to gain access to functions such as authentication, information retrieval from a database, and cookie management.


### Overview

<img src="./img/WebAppDiagram.jpg" alt="webappdiagram" />


The web application is devided into three sections.

- Server: Host the web application logic as well as the database server.
- User Clients: Researcher devices that access the web application's functions via a web browser.
- Device Clients: A cage-based device embedded with a Python script to automate the web browser for accessing the experimental application, manipulate the GPIO of the integrated system, and invoke API calls to the server backend to perform CRUD operations on the database.


### Server

#### Database

To centalize the system and allow mutiple intruments to work simutinueously. We have stored the state of the entire system in the database server.

For instance, we reference each cage-based device in the RPIBOARDS table, storing its name, IP address, and other relevant information. We can define this using a Django model like this:

```
class RPiBoards(models.Model):
    board_name = models.CharField(max_length=255, default="")  
    ip_address = models.GenericIPAddressField(protocol='IPv4') 
    ssid = models.CharField(max_length=32 , blank=True , null=True) 
    ssid_password = models.CharField(max_length=255, blank=True , null=True)  
    def __str__(self)-> str:
	    return self.board_name

```

We also have the RPISTATES table for each device, which allows the instrument to track whether or not to run or end a task. This table also stores the state of the GPIO, enabling the edge device (the Raspberry Pi, in this case) to manipulate the peripherals.

```
class RPiStates(models.Model):
    rpiboard = models.OneToOneField(RPiBoards, on_delete=models.CASCADE)
    is_occupied =  models.BooleanField(default=False)
    game_instance_running = models.IntegerField(default=None,  blank=True , null=True) 
    start_game =  models.BooleanField(default=False)
    stop_game =  models.BooleanField(default=False)
    motor = models.BooleanField(default=False)
    def __str__(self)-> str:
	    return self.rpiboard.board_name
```

When it comes to the tasks, each device runs a different experiment instance (which may also involve different tasks). It is crucial to keep track of these states to manage the simultaneous operation of multiple instruments.

An example of the GAMEINSTANCE table allows us to keep track of each task's information, such as which instrument is being used, which task is being performed, which primate is involved, the configuration profile, and other relevant details.

```
class GameInstances(models.Model):
    name = models.CharField(max_length=255)
    game = models.ForeignKey(Games, on_delete=models.PROTECT)
    config = models.ForeignKey(GameConfig, on_delete=models.PROTECT, related_name="gameconfig")
    rpiboard = models.ForeignKey(RPiBoards, on_delete=models.PROTECT , related_name="rpiboard")
    primate = models.ForeignKey(Primates, on_delete=models.PROTECT , related_name="primate")
    login_hist = models.DateTimeField()
    logout_hist = models.DateTimeField(blank=True , null=True)
    def __str__(self)-> str:
	    return self.name
```

Another crucial part is the experiment result of each task. This web application platform supports report generation, so we need to design the database carefully to ensure that the results of each task instance are stored properly.

One way we can do this is by creating a REPORT table to separate each task's report. We would then create two additional tables based on the task: one table for the instance of the report and another table to store the actual result of the task.

```
class Reports(models.Model):
    reportname =  models.CharField(max_length=50)
    game = models.ForeignKey(Games, on_delete=models.PROTECT)
    def __str__(self)-> str:
	    return self.reportname

class FixationGameReport(models.Model):
    report = models.ForeignKey(Reports, on_delete=models.PROTECT)
    instance = models.OneToOneField(GameInstances, on_delete=models.PROTECT,related_name="fixationreportgameinstance")
    gamereportname = models.CharField(max_length=50, blank=True , null=True)
    def __str__(self)-> str:
	    return self.gamereportname
    
class FixationGameResult(models.Model):
    fixationreport = models.ForeignKey(FixationGameReport, on_delete=models.PROTECT)
    timestamp = models.DateTimeField()
    feedback = models.BooleanField()
    feedbacktype = models.CharField(max_length=10)
    buttonsize = models.FloatField()
    def __str__(self)-> str:
	    return self.fixationreport.gamereportname

```

#### Web application 
The web application is powered by the Django framework. The reason for this is that having a clear separation between the different parts allows the system to scale for various tasks. By separating application servers, we can create the logic for multiple tasks without interfering with each other. Another benefit is that Django promotes the grouping of related functionality into reusable "applications" and, at a lower level, organizes related code into modules.

The core components of this project are listed as follows:

- Web appplication logic
- API server
- User authentication/authorization application (via djoser and Django REST framework)
- Tasks application

#### User Clients

User clients are researchers and observers who can access the web application remotely to start or stop the experiment on each device, monitor the status of the experiment, or download reports.

With the convenience of the Django template language, the web application's front end can update content dynamically from the database.

The Django Template Language (DTL) is a built-in templating system in Django used to generate dynamic HTML content. It allows developers to embed Python-like expressions inside HTML files while maintaining separation between logic and presentation.

Some of the core function of the Web application platform on user clients side:

- User authentication/authorization with tokenization, session management.</br>
<img src="./img/login.png" alt="login" width="300"/>

- Remotely controlled experiments on the edge device with customized configurations for each task.
<img src="./img/startgame.png" alt="startgame" />

- Dynamically update the state of each device in real-time, observe the experiment results, and end the session.
<img src="./img/state1.png" alt="state1" />
<img src="./img/state2.png" alt="state2" />

- Report generation: Support filtering by date, tasks, and optionally by instruments and primates.
<img src="./img/reportgeneration.png" alt="reportgeneration" />


#### Device Clients

Device clients, also known as cage-based devices in this project, are Raspberry Pi-based systems that also gain access to the web application, but as RPiClients users. The token from this user allows the server to grant permission for each device client to perform CRUD operations via APIs.

<img src="./img/userclientflow.png" alt="userclientflow" />

The device clients are installed with Python scripts that leverage Selenium to automate the Chromium web browser.

When the system is booted, it is automatically logged in with its own credentials, connects to the web application, and enters power-saving mode, waiting for instructions.

The Python script keeps querying its own status at fixed intervals. When the user client makes an experiment request, the device switches to the corresponding task.

Also, the GPIOs are manipulated according to status updates from the database, and when the task sends an update request for each GPIO, the system sends a PATCH operation to update its own state.

## Task: Experiment Application

Tasks for each experiment can be built using only plain JavaScript, with the help of the Django template language. Each task can use AJAX to create dynamic and interactive web pages, allowing data to be exchanged between the web browser and the server asynchronously, without reloading the entire page.

### Fixation Task

Our first implemented task is the fixation task. a fixation task refers to an experimental task designed to study visual attention, eye movements, cognitive processes and neural mechanisms involved in gaze control, decision-making, and perception.


The goal of the training was to instruct common marmosets to interact with the touchscreen in order to receive a liquid reward (fruit juice) from the device’s mouthpiece. 

In order to receive a liquid reward, a primate must touch inside the button for a short period of time (due to touchscreen sensitivity). After that, it transitions to the "correct" state (turns to a green button), and the primate receives a liquid reward.

The other state is 'incorrect' (turns to a red button), which can occur in two cases.
- A primate touched the background of the screen, missing the button.
- The button is ignored for a fixed duration.

In both cases, the output is recorded in the database.


<img src="./img/fixation1.png" alt="fixation1" /></br>


Logic of the task

1. Reduction in size of the button: The size of the button will be reduced by a fixed percentage of the initial size (which can be configured) if 9 out of 10 recent trials are in the 'correct' state. At the start of the trial, the button will occupy 95% of the screen.

2. Randomization of the positions: After each state, the button is repositioned to a random point within the boundary of the screen.

3. Size threshold and overlay: The button cannot be reduced indefinitely. At a certain threshold (0.5 cm), it will maintain the same size. A transparent window is created around the button to reduce noise.


#### Now our monkey can learn how to use a touchscreen!