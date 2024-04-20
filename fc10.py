#fuction code = 10     /     16

ctx.rule("START", "{MBAP}{PDU}\n")   

ctx.rule("MBAP", "{Tid}{Pid}00{Length}{Uid}")

ctx.script("Length", ["Len"], lambda leng:'{:02x}'.format(len(leng)//2))

ctx.rule("Len", "{Uid}{PDU}")

ctx.rule("PDU", "{FC}{Data}")

ctx.rule("Tid", "{T_Byte}{T_Byte}")

ctx.rule("Pid", "0000")

ctx.rule("Uid", "01")

ctx.rule("FC", "10")

ctx.rule("Data", "{Data_addr}{Register_num}{Byte_num}{Write_Data}")

ctx.script("Data_addr", ["Byte1"], lambda num: str('{:04X}'.format(int(num))))

ctx.script("Register_num", ["Write_Data"], lambda write_Data1: '{:04x}'.format(len(write_Data1)//4))

ctx.script("Byte_num", ["Write_Data"], lambda write_Data1:'{:02x}'.format(len(write_Data1)//2))

ctx.rule("Write_Data", "{Byte}")

ctx.regex("T_Byte", "(?:[0-9A-F]{2}|[0-9a-f]{2})|(?:[0-9A-F]{2}|[0-9a-f]{2})")

ctx.regex("D_Byte", "(?:[0-9A-F]{2}|[0-9a-f]{2})|(?:[0-9A-F]{2}|[0-9a-f]{2})")

ctx.regex("Byte", "(?:[0-9A-F]{4}|[0-9a-f]{4})|(?:[0-9A-F]{4}|[0-9a-f]{4})")

ctx.regex("Byte1", "(?:[0-9]|[1-9][0-9]|[1-3][0-9]{2}|40[0-8][0-9]|409[0-6])")