import binascii

hexdata = ''
hexdata_as_ascii_text = ''
# Replace in.txt with any file you like:
with open('in.txt', 'rb') as f:
    hexdata = f.read()
    hexdata_as_ascii_text = hexdata.hex()

index = 0
total_hex_values_overwritten = 0
write_back_string = ''

# Overwrite every 10th hex value with "F"
for index in range(len(hexdata_as_ascii_text)):
    if(index % 10 == 1):
        # Set to any Hex value 0-9 A-F:
        char_to_overwrite_with = 'f'
        write_back_string += chr(ord(char_to_overwrite_with))
        # Only tally it in the number of changed values if it changed.
        if(hexdata_as_ascii_text[index] != char_to_overwrite_with):
            total_hex_values_overwritten = total_hex_values_overwritten + 1
    else:
        write_back_string += chr(ord(hexdata_as_ascii_text[index]))
    
# Write out the result. Replace out.txt with any file you like:
with open('out.txt', 'wb') as fout:
    fout.write(binascii.unhexlify(write_back_string))

print('The program overwrote ' + str(total_hex_values_overwritten) + ' of ' + str(len(hexdata_as_ascii_text)) + ' total hex values.' )