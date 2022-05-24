# Noddy Shifter

author: pfgs (github.com/stripboard-layouts)  
date: 2022-05-24
labels: asr, gates, sample&hold, track&hold

Sample & hold, track & hold, and analog shift register based on Noddy Holder by Sean Bechhofer. I havn't asked him yet if the name is OK.

As per Noddy Holder:
  Digital in is a gate, Analog in is arbitrary CV.
  Output 1 is the original gate, Output 2 is S&H based on gate and CV,
  Ouput 3 is T&H based on gate and CV.

Outputs 4, 5 and 6 are the analog shift register, where the previous samples are cascaded down as the new one is taken.

Credits:
- The Europi hardware and firmware was designed by Allen Synthesis: https://github.com/Allen-Synthesis/EuroPi

# Controls

- digital_in: Gate
- analog_in: CV

- knob_1: 
- knob_2: 

- button_1: 
- button_2: 

- output_1: gate 
- output_2: s&h based on gate
- output_3: t&h based on gate
- output_4: previous sample
- output_5: previous sample once removed
- output_6: previous sample twice removed

## Basic Usage
1. Switch on
2. Connect outputs to modules
3. Send gate and CV to inputs
4. Send resulting gates and CV to modules

## Controls
1. There are still no controls.

## Details

*Sample & Hold:* When gate goes ```HIGH```, CV is sampled, and the resulting value is
output until the gate goes ```HIGH``` again and we re-sample.

*Track & Hold:* When gate is ```HIGH```, CV input is mirrored to the
output. When gate goes ```LOW```, CV is sampled and the resulting value is
output until the gate goes ```HIGH``` again. 
