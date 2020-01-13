# RaspbianPLCcontrol
Just a demo using pymodbus for PLC's

I did not create any of the imports used but This is simply demo code that works triggering PLC's VIA modbus

Example

C0 is the lowest address available on the PLC

remove the "C"

address of 0 in this case is  3073 according to the datasheet

C1006 is what I want to trigger.

Remove the "C"

1006 in octals gives 518 in decimal (you can look this up on rapidtables if you're feeling ultra lazy)

518 + 3073 = 3591

3591 THEN becomes what you try to trigger

c.write_single_coil(3591, TRUE)  will trigger C1006.  FALSE will open the relay
