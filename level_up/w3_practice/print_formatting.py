"""
% is called String Modulo operator
String formatting placeholder syntax: %[flags][width][.precision]type

+------------+----------------------------------+
|Conversion  |  Meaning                         |
+------------+----------------------------------+
|      d     |  Decimal integer                 |
|      b     |  Binary format                   |
|      o     |  octal format                    |
|      u     |  Obsolete and equivalent to ‘d’  |
| x or X     |  Hexadecimal format              |
| e or E     |  Exponential notation            |
| f or F     |  Floating-point decimal          |
| g or G     |  General format                  |
|      c     |  Single Character                |
|      r     |  String format(using repr())     |
|      s     |  String Format(using str()))     |
|      %     |  Percentage                      |
+------------+----------------------------------+

"""

print("Geeks: %2d, portal: %5.2f" % (1, 05.33))
print("Total Students: %3d, Boys: %2d" % (240, 120))
print("%7.3o" % 25)
print("%10.3E" % 356.08977)
