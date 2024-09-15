import os
from time import time
import binascii
import math
import os.path
import sys

# @Author Jurijus Pacalovas
# Get the name of the current script

if os.path.basename(sys.argv[0]) != 'Black_Hole_44.py':
    sys.exit("This is not 'Black_Hole_44.py'.")

print("The script 'Black_Hole_44.py' is currently running.")


class compression:

    def cryptograpy_compression4(self):

        def process_file1(Extract1=0, File_information5_17="Ex", name="", x=0):
            if Extract1 == 1:
                with open(name + ".b", "wb") as f2:
                    f2.write(
                        binascii.unhexlify(
                            (
                                "%0"
                                + str((len(File_information5_17) // 8) * 2)
                                + "x"
                            )
                            % int(File_information5_17, 2)
                        )
                    )
                    return str(time() - x)

        def process_file(Extract1=0, File_information5_17="Ex", name="", x=0):
            if Extract1 == 1:
                width_bits = (
                    "%0" + str((len(File_information5_17) // 8) * 2) + "x"
                ) % int(File_information5_17, 2)
                with open(name[:-2], "wb") as f2:
                    f2.write(binascii.unhexlify(width_bits))
                    return str(time() - x)

        def Count_adds(En, Row1, Row):

            Row += 1

            if Row == (8192 * 4) - 1:
                Row = 0

            if En == (8192 * 4) - 1:
                En = 255
            En += 1

            return En, Row1, Row

        import re

        def find_smallest_longl_F_values(input_string):

            # Extract all 'En', 'En2', 'Row', and 'Longl_F' values

            pattern = r'En=(\d+), Longl_F=(\d+)'

            matches = re.findall(pattern, input_string)

            # Convert the extracted strings to tuples of integers

            longl_F_values = [
                (int(en), int(longl_f)) for en, longl_f in matches
            ]

            if longl_F_values:

                # Find the smallest 'Longl_F' value and its corresponding variables

                smallest_longl_F_values = min(
                    longl_F_values, key=lambda x: x[1]
                )

                return smallest_longl_F_values

            else:

                return None

        self.name = "Written: Jurijus pacalovas"

        N5 = 1

        if N5 == 1:

            Clear = ""

            name = input("What is name of file input? ")

            long_21 = len(name)

            name_f = name[long_21 - 2 :]

            if name_f == ".b":

                i = 2

            else:

                i = 1

            # print(i)
            if os.path.exists(name):

                print('Path is exists!')

            else:

                print('Path is not exists!')

                raise SystemExit

            x = 0
            C1 = 1
            x1 = 0
            x2 = 0
            x3 = 0
            X2 = 0
            C1 = 0
            C2 = 0
            C3 = 0
            C4 = 0
            ZEROS_ONE_1 = ""
            Circle_times = 0
            Circle_times2 = 1
            Circle_times3 = 0
            CB = -1
            x = time()
            File_information6_Times2_1 = 0
            name_2 = name
            Long_Change = len(name_2)
            compress_or_not_compress = 1

            File_information6_Times3 = 0

            if i == 2:

                C = 1

            Long_Change = len(name_2)
            s = ""
            File_information5 = ""
            File_information5_2 = ""
            Clear = ""
            Translate_info_Decimal = ""
            D = 0
            long_name = len(name)
            with open(name, "rb") as binary_file:

                data = binary_file.read()
                s = str(data)

                long_11 = len(data)

                long_17 = len(data)

                if long_17 == 0:

                    raise SystemExit

                END_working = 0

                File_information6_Times2 = 0

                File_information5_23 = ""

                INFO18 = ""

                File_information5_29 = ""

                SpinS = 0

                while END_working < 10:

                    File_information6_Times3 = File_information6_Times3 + 1

                    D = 1

                    if D == 1:

                        if File_information6_Times3 == 1:

                            INFO = bin(int(binascii.hexlify(data), 16))[
                                2:
                            ]  # data to binary

                            long_1 = len(INFO)

                            long_11 = len(data)

                            count_bits = (long_11 * 8) - long_1

                            z = 0

                            if count_bits != 0:

                                while z < count_bits:

                                    INFO = "0" + INFO

                                    z = z + 1

                            if File_information6_Times3 == 1:

                                File_information5_2 = INFO

                            n = int(File_information5_2, 2)

                            width_bits = len(File_information5_2)

                            width_bits = (width_bits / 8) * 2

                            width_bits = str(width_bits)

                            width_bits = "%0" + width_bits + "x"

                            width_bits3 = binascii.unhexlify(width_bits % n)

                            width_bits2 = len(width_bits3)

                            data = width_bits3

                            long_15 = len(data)

                            INFO = bin(int(binascii.hexlify(data), 16))[2:]

                            long_1 = len(INFO)

                            long_11 = len(data)

                            count_bits = (long_11 * 8) - long_1

                            z = 0

                            if count_bits != 0:

                                while z < count_bits:

                                    INFO = "0" + INFO

                                    z = z + 1

                            Check = INFO

                            File_information5_2 = INFO

                            Extact = File_information5_2

                            A = int(Extact, 2)
                        long_13 = len(File_information5_2)

                        long_12 = len(File_information5_2)

                        if i == 1:

                            if long_17 > (2**28) - 1 and i == 1:

                                print("print file is too big!")

                                raise SystemExit

                        if i == 1:

                            Ex = 1

                            if Ex == 1:

                                Extract1 = 0

                                Find = 0

                                En = 3

                                Ci = 1

                                M1 = 0

                                Row1 = 0

                                input_string = ""

                                C1 = ""

                                Row = 0

                                I8 = INFO

                                W3 = ""

                                W4 = ""

                                block = 0

                                IF1 = ""

                                long_F = len(I8)

                                # print(long_F)

                                FC = 0

                                IF2 = ""

                                Z7 = 0

                                CZ = 0

                                if Circle_times == 0:

                                    SINFO = ""

                                    TUPLE = INFO

                                if Circle_times == 0:

                                    SINFO = INFO
                                long_bits_after=0
                                long_bits_after_b=0
                                long_bits_before=0
                                times_compress=0
                                long_after_bits=0
                                long_bits_after_b_1=0
                                J=1
                                long_F1=long_F
                                while times_compress!=10:


                                	block=0
                                	long_after_bits=len(INFO)
                                	Transform=INFO
                                	T10=""
                                	c_c=0
                                	while block<long_F:
                                		times_c_c=0
                                		T8=Transform[block:block+19]
                                		
                                		if c_c==0:
                                			num=int(T8,2)
                                			#print(num)
                                			c_c=1
                            
                                		block+=19
                                		long_bits_after_1=0
                                		finish=0
                                		times=0
                                		num = num
                                		#print("num")
                                		#print(num)
                                		binary_representation_before=len(format(num,'01b'))
                                		#print("binary_representation_before_long")
                                		#print(binary_representation_before)
                                		while finish!=1:
                                			if num < 0:
                                				print("Please enter a non-negative integer.")
                                			else:
                                				max_length = len(format(num, 'b'))
                                				binary_numbers = []
                                			for length in range(1, max_length + 1):
                                				for i in range(2 ** length):
                                					binary_numbers.append(format(i, '0' + str(length) + 'b'))
                                			last_binary = None
                                			for index, binary in enumerate(binary_numbers):
                                			   		if index > num:
                                			   			break
                                			last_binary = (binary, index)
                                			if last_binary:
                                			   	binary_representation, index = last_binary
                                			   	#print(f"{binary_representation}: {index}")
                                			   	binary_to_number=int(binary_representation,2)
                                			
                                			   	binary_representation=format(binary_to_number,'08b')
                                			   	num=binary_to_number
                                			   	#print(num)
                                			   	
                            
                                			  
                                			   	binary_to_number_number_after=binary_to_number
                                			   	#print("binary_to_number")
                                			   	
                                			   	print(binary_to_number)
                                			   	binary_to_number_after=binary_to_number
                                			   	length_tree=len(binary_representation)
                                			   	times+=1
                                			   	#print("times")
                                			   	#print(times)
                                			   	#print("length_tree")
                                			   	#print(str(length_tree))
                                			   	if length_tree<9:
                                			   		finish=1
                                			   		c_c=0
                                			   		#print(c_c)
                                			   		length_tree_after=length_tree
                                			   		times_after=times
                                			   		binary_representation_before_long=binary_representation_before
                                			   		binary_representation_before_long1=format(binary_representation_before,'05b')
                                			   		length_tree_after=format(binary_representation_before,'05b')
                                			   		T10+=binary_representation+length_tree_after+binary_representation_before_long1	      

                                	INFO=T10	
                                	long_bits_after_b_1=1
                                	block=0 
                                	times_compress+=1                         		
                                                          		

                                		
                                		
                                Compress_file=1
                                #print(Compress_file)                              	     
                                if Compress_file==1:
                                    times_compression_format=format(long_bits_after_b,'01b')
                                    times_255=format(len(times_compression_format), '08b')
                                    times_compression_format_255=format(times_compress,'01b')
                                    times_255_long_after_bits=format(len(times_compression_format_255), '08b')
                                    I_F=format(long_F1, '040b')
                                    
                                    
                                    File_information5_17=times_255_long_after_bits+times_255+times_compression_format+times_compression_format_255+I_F+INFO
                                    n = int(File_information5_17, 2)
                                    width_bits = "%0{}x".format(
                                        (len(File_information5_17) // 8) * 2
                                    )
                                    jl = binascii.unhexlify(width_bits % n)
                                    with open(f"{name}.b", "wb") as f2:
                                        f2.write(jl)
                                    x3 = time() - x
                                    print(f"Speed bits: {long_11 / x3:.5f}")
                                    return str(float(x3))

                        if i == 2:

                            if C == 1:

                                Extract1 = 0

                                if File_information6_Times2 == 0:

                                    File_information5 = INFO

                                    Extract = 0

                                    Ex = INFO

                                    if Ex[:8] == "00000000":

                                        L = len(Ex[8:])

                                        File_information5_17 = Ex[8:]

                                        n = int(File_information5_17, 2)

                                        width_bits = len(File_information5_17)

                                        width_bits = (width_bits // 8) * 2

                                        width_bits = str(width_bits)

                                        width_bits = "%0" + width_bits + "x"

                                        width_bits3 = binascii.unhexlify(
                                            width_bits % n
                                        )

                                        width_bits2 = len(width_bits3)

                                        File_information5_2 = Clear

                                        jl = width_bits3

                                        long = len(name)

                                        name2 = name[: long - 2]

                                        with open(name2, "wb") as f2:

                                            f2.write(width_bits3)

                                        x2 = time()

                                        x3 = x2 - x

                                        xs = float(x3)

                                        xs = str(xs)

                                        return xs

                                    if Circle_times3 == 0:

                                        long_16 = len(File_information5)

                                        if File_information5[:1] == "0":

                                            while File_information5[:1] != "1":

                                                if File_information5[:1] == "0":

                                                    File_information5 = (
                                                        File_information5[1:]
                                                    )

                                        if File_information5[:1] == "1":

                                            File_information5 = (
                                                File_information5[1:]
                                            )

                                    INFO = File_information5

                                    if Circle_times3 == 0:

                                        Circle_times4 = int(INFO[:8], 2)

                                        # print(Circle_times4)

                                        INFO = INFO[8:]

                                    while Extract1 != 1:
                                    	


                                        
                                        TUPLE=INFO
                                        long_L = len(TUPLE)

                                        # print(long_L)

                                        N3 = 1

                                        # print(N3)

                                        if N3 == 1:

                                            N3 = 1

                                            block = 0

                                            long_F = len(TUPLE)

                                            Z = TUPLE

                                            Z6 = ""

                                            Z7 = 0

                                            TUPLE1 = Z

                                            cut_b = 0

                                            long_F = len(TUPLE)

                                            while block < long_F:

                                                E = Z[block : block + 1]

                                                if E == "0" and Z7 == 0:

                                                    cut_b = 1

                                                    block += 1

                                                    E2 = Z[block : block + 8]

                                                    block += 8

                                                    E3 = int(
                                                        Z[block : block + 5], 2
                                                    )

                                                    block += 5

                                                    S5 = Z[block : block + E3]

                                                    if len(S5) == 0:

                                                        Extract1 = 0

                                                        File_information5_17 = (
                                                            Ex
                                                        )

                                                        elapsed_time = process_file(
                                                            Extract1=1,
                                                            File_information5_17=File_information5_17,
                                                            name=name,
                                                            x=x,
                                                        )

                                                        return elapsed_time

                                                    E1 = int(
                                                        Z[block : block + E3], 2
                                                    )

                                                    block += E3

                                                    TUPLE4 = int(
                                                        Z[block : block + 5], 2
                                                    )

                                                    block += 5

                                                    E5 = int(
                                                        Z[
                                                            block : block
                                                            + TUPLE4
                                                        ],
                                                        2,
                                                    )

                                                    block += TUPLE4

                                                    b = 0

                                                    E3 = ""

                                                    while b < E5 - 1:

                                                        E3 += E2

                                                        b += 1

                                                        # print(E2)

                                                    TUPLE1 = TUPLE1[block:]
                                                    E1 *= 8

                                                    TUPLE1 = (
                                                        TUPLE1[:E1]
                                                        + E3
                                                        + TUPLE1[E1:]
                                                    )

                                                    block += long_F

                                                elif E == "1" or Z7 == 1:

                                                    block += 1

                                                    Z7 = 1

                                                    if cut_b == 0:

                                                        TUPLE1 = TUPLE1[block:]

                                                        cut_b = 1

                                                        block += long_F

                                                        # print(block)

                                                # print(block)

                                            # print(Long_PM1)

                                            TUPLE = TUPLE1

                                            # print(len(TUPLE))

                                            N3 = 1

                                            Circle_times += 1

                                            # print(Circle_times)

                                            INFO = TUPLE

                                            Extract1 = 0

                                            N3 = 0

                                            # print(len(TUPLE))

                                            # print(Circle_times4)

                                            if Circle_times == Circle_times4:

                                                Extract1 = 1

                                                N3 = 2

                                            if N3 == 2:

                                                File_information5_17 = TUPLE

                                                long_1 = len(
                                                    File_information5_17
                                                )

                                                add_bits = ""

                                                count_bits = 8 - long_1 % 8

                                                z = 0

                                                if count_bits != 0:

                                                    while z < count_bits:

                                                        add_bits = (
                                                            "0" + add_bits
                                                        )

                                                        z = z + 1

                                                File_information5_17 = (
                                                    File_information5_17
                                                )

                                                if Extract1 == 1:
                                                    L = len(
                                                        File_information5_17
                                                    )
                                                    n = int(
                                                        File_information5_17, 2
                                                    )
                                                    width_bits = (
                                                        "%0"
                                                        + str((L // 8) * 2)
                                                        + "x"
                                                    )
                                                    width_bits3 = (
                                                        binascii.unhexlify(
                                                            width_bits % n
                                                        )
                                                    )
                                                    width_bits2 = len(
                                                        width_bits3
                                                    )
                                                    name2 = name[:-2]
                                                    start_time = time()
                                                    with open(
                                                        name2, "wb"
                                                    ) as f2:
                                                        f2.write(width_bits3)
                                                    elapsed_time = (
                                                        time() - start_time
                                                    )
                                                    speed_bits = (
                                                        long_11 * 8
                                                    ) / float(elapsed_time)
                                                    print(
                                                        f"Speed bits: {speed_bits:.5f}"
                                                    )
                                                    return str(elapsed_time)


d = compression()
xw1 = d.cryptograpy_compression4()
print(xw1)
