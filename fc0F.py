#fuction code = 0F   /   15

ctx.rule("START", "{MBAP}{PDU}\n")   

ctx.rule("MBAP", "{Tid}{Pid}00{Length}{Uid}")

ctx.script("Length", ["Len"], lambda leng:'{:02x}'.format(len(leng)//2))

ctx.rule("Len", "{Uid}{PDU}")

ctx.rule("PDU", "{FC}{Data}")

ctx.rule("Tid", "{Byte}{Byte}")

ctx.rule("Pid", "0000")

ctx.rule("Uid", "01")

ctx.rule("FC", "0F")

ctx.rule("Data", "{Data_addr}{Data_num}{Byte_num}{Data_value}")

ctx.script("Data_addr", ["Byte1"], lambda num1: str('{:04X}'.format(int(num1))))

ctx.script("Data_num", ["Byte2"], lambda num2: str('{:04X}'.format(int(num2))))

ctx.rule("Byte_num", "01")

ctx.rule("Data_value", "{Byte}")

ctx.regex("Byte", "(?:[0-9A-F]{2}|[0-9a-f]{2})|(?:[0-9A-F]{2}|[0-9a-f]{2})")

ctx.regex("Byte1", "(?:[0-9]|[1-9][0-9]|[1-3][0-9]{2}|40[0-8][0-9]|409[0-6])")

ctx.regex("Byte2", "(?:[0-8])")