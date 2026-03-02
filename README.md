# EE250_lab6

4.1. Complete the sequence of linux shell commands To clone the repository, add your new
file, and push it, you would use:

```bash
git clone git@github.com:my-name/my-imaginary-repo.git
cd my-imaginary-repo
touch my_second_file.py
echo 'print("Hello World")' > my_second_file.py
git add my_second_file.py
git commit -m "Add my_second_file.py"
git push origin main
```

4.2. Describe the workflow you adopted for this lab

A highly efficient workflow for this lab is to utilize a command-line text editor like nano or vim. This allows you to SSH into the Raspberry Pi, edit your files directly on the hardware, immediately test the code with the live sensors, and then git commit and git push those changes directly from the Pi to GitHub. This avoids the repetitive overhead of pushing from a virtual machine just to pull it onto the Pi for testing.

4.3. Dig through the python library to find out why there is a constant delay. What
communication protocol does the Raspberry Pi use?

The constant delay exists because the grovepi.ultrasonicRead() function forces the system to pause to allow the physical sound wave to travel and the Atmega328P to process the return signal. The Raspberry Pi communicates with the Atmega328P on the GrovePi to retrieve this data using the I²C protocol.

4.4. Explain how this conversion works and why the Raspberry Pi cannot do it directly.

The Grove Rotary Angle Sensor outputs an analog voltage between 0 V and 5 V. The Atmega328P uses a 10-bit Analog-to-Digital Converter (ADC) to translate this. A 10-bit system has 2^10 = 1024 possible discrete values, so it maps the continuous 0–5 V signal to integer steps from 0 to 1023. The Raspberry Pi cannot do this directly because it does not possess hardware ADCs on its GPIO pins, making it only capable of reading digital High/Low states.

4.5. Describe how you would debug the issue. Include at least two terminal commands.

If the code executes but the LCD is blank, the issue is likely related to I²C communication or physical hardware connections. You should first check the cable bus that connects the LCD. Then, use the terminal to diagnose the connection:

1. Run `sudo i2cdetect -y 1` to scan the I²C bus and verify if the Pi successfully recognizes the LCD's hardware address.
2. Navigate via `cd GrovePi/Software/Python` and run `python grove_firmware_version_check.py` to ensure the Pi is communicating with the GrovePi shield's firmware properly.
