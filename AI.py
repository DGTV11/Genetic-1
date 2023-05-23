from random import *
from merge_sort import *
from radix_sort import *
from filtered_intepreter import *
from obj2file import *
import os

def AI(save_path, targettext, max_genome_length, gs): #Note: max_genome_length is now just default maximum genome length!
    o = OTF(save_path)
    targetreached = False
    generation = list()
    generation_no = 1
    gen_size = gs
    genome = list()
    bestgenomes = list()

    if os.path.isfile(save_path):
        if os.stat(save_path).st_size != 0:
            try:
                l = o.pull_bulk()
                generation_no = l[0]
                gen_size = l[1]
                generation = l[2]
            except EOFError:
                os.remove(save_path)

    print("GENETIC AI START")
    
    cmdlist = {
        1   : "<",
        2   : ">", 
        3   : "+", 
        4   : "-", 
        5   : ".", 
        6   : ",", 
        7   : "[", 
        8   : "]",
        9   : "^", 
        10  : "v",
        11  : "'",
        12  : ";",
        13  : "*",
        14  : "~",
        15  : "}",
        16  : "{",
        17  : "`",
        18  : "_",
        19  : "@",
        20  : "|",
        21  : "/",
        22  : ":",
        23  : "=",
        24  : "!",
        25  : "$",
        26  : "#",
        27  : "%",
        28  : "(",
        29  : ")"
    }

    while not targetreached:
        performancelist = dict()
        unsortedperformancekeys = list()
        sortedperformancekeys = list()

        if bestgenomes == list():
            for i in range(gen_size):
                for i in range(randint(5, max_genome_length)):
                    genome.append(randint(1, 29))
                generation.append(genome)
                genome = list()
        else:
            for i in range(gen_size):
                genome_of_choice = choice(bestgenomes)
                second_genome_of_choice = choice(bestgenomes)
                third_genome_of_choice = choice(bestgenomes)
                if round((len(genome_of_choice) + len(second_genome_of_choice))/2) > max_genome_length:
                    genome_length = max_genome_length
                else:
                    genome_length = round((len(genome_of_choice) + len(second_genome_of_choice))/2)

                if randint(0, 100) <= 80 or (not genome_length >= max_genome_length): # Tries to do Mix_n_match only
                    # instability_type = randint(-1, 1)
                    # if instability_type == -1:
                    #     genome_length - randint(1, 20)
                    # elif instability_type == -1:
                    #     pass
                    # else:
                    #     genome_length + randint(1, 20)

                    for i in range(genome_length):
                        if randint(1, 2) == 1:
                            try:
                                genome.append(genome_of_choice[i])
                            except IndexError:
                                try:
                                    genome.append(second_genome_of_choice[i])
                                except IndexError:
                                    genome.append(randint(1, 29))
                        else:
                            try:
                                genome.append(second_genome_of_choice[i])
                            except IndexError:
                                try:
                                    genome.append(genome_of_choice[i])
                                except IndexError:
                                    genome.append(randint(1, 29))

                else: # Mix_n_match + Mutation
                    if (not genome_length == max_genome_length) and (not randint(1, 5) < 3):
                        # instability_type = randint(-1, 1)
                        # if instability_type == -1:
                        #     genome_length - randint(1, 15)
                        # elif instability_type == -1:
                        #     pass
                        # else:
                        #     genome_length + randint(1, 15)
                        for i in range(genome_length):
                            randomiser = randint(1, 3)
                            if randomiser == 1:
                                try:
                                    genome.append(genome_of_choice[i])
                                except IndexError:
                                    try:
                                        genome.append(second_genome_of_choice[i])
                                    except IndexError:
                                        genome.append(randint(1, 29))
                            elif randomiser == 2:
                                try:
                                    genome.append(second_genome_of_choice[i])
                                except IndexError:
                                    try:
                                        genome.append(genome_of_choice[i])
                                    except IndexError:
                                        genome.append(randint(1, 29))
                            else: # Mutate!
                                genome.append(randint(1, 29))
                    else:
                        randomiser = randint(2, 3)
                        if randomiser == 2:
                            instability_type = randint(-1, 1)
                            if instability_type == -1:
                                genome_length - randint(1, 10)
                            elif instability_type == -1:
                                pass
                            else:
                                genome_length + randint(1, 10)

                            for i in range(genome_length):
                                randomiser = randint(1, 2)
                                if randomiser == 1:
                                    randomiser = randint(1, 2)
                                    if randomiser == 1:
                                        try:
                                            genome.append(genome_of_choice[i])
                                        except IndexError:
                                            try:
                                                genome.append(second_genome_of_choice[i])
                                            except IndexError:
                                                genome.append(randint(1, 29))
                                    else:
                                        try:
                                            genome.append(second_genome_of_choice[i])
                                        except IndexError:
                                            try:
                                                genome.append(genome_of_choice[i])
                                            except IndexError:
                                                genome.append(randint(1, 29))
                                else: # Mutate!
                                    genome.append(randint(1, 29))
                        elif randomiser == 3:
                            l_choices = [
                                round(choice([(len(genome_of_choice) + len(second_genome_of_choice)), (len(second_genome_of_choice) + len(third_genome_of_choice)), (len(third_genome_of_choice) + len(genome_of_choice))]) /2 ),
                                round((len(genome_of_choice) + len(second_genome_of_choice) + len(third_genome_of_choice)) / 3)
                            ]

                            x = randint(1, 5)
                            genome_length = choice(l_choices)+randint(-x, x)

                            instability_type = randint(-1, 1)
                            if instability_type == -1:
                                genome_length - randint(1, 5)
                            elif instability_type == -1:
                                pass
                            else:
                                genome_length + randint(1, 5)

                            for i in range(genome_length):
                                randomiser = randint(1, 2)
                                if randomiser == 1:
                                    randomiser = randint(1, 3)
                                    if randomiser == 1:
                                        try:
                                            genome.append(genome_of_choice[i])
                                        except IndexError:
                                            try:
                                                genome.append(second_genome_of_choice[i])
                                            except IndexError:
                                                try:
                                                    genome.append(third_genome_of_choice[i])
                                                except:
                                                    genome.append(randint(1, 29))
                                    elif randomiser == 2:
                                        try:
                                            genome.append(second_genome_of_choice[i])
                                        except IndexError:
                                            try:
                                                genome.append(third_genome_of_choice[i])
                                            except IndexError:
                                                try:
                                                    genome.append(genome_of_choice[i])
                                                except IndexError:
                                                    genome.append(randint(1, 29))
                                    else:
                                        try:
                                            genome.append(third_genome_of_choice[i])
                                        except IndexError:
                                            try:
                                                genome.append(genome_of_choice[i])
                                            except IndexError:
                                                try:
                                                    genome.append(second_genome_of_choice[i])
                                                except IndexError:
                                                    genome.append(randint(1, 29))
                                else: # Mutate!
                                    genome.append(randint(1, 29))

                generation.append(genome)
                genome = list()

        for genome in generation:
            performanceevalkey = int()
            performanceeval = list()
            code = str()

            performanceeval.append(genome)
            for item in genome:
                code += cmdlist[item]
            performanceeval.append(code)

            intepreter_barf = filtered_intepreter(code, targettext)

            performanceevalkey = intepreter_barf[0]
            performanceeval.append(intepreter_barf[1])

            performancelist.update({performanceevalkey : performanceeval}) # fitness : [genome(list), translatedgenome(str), filtered_output(str)] 
        for key in performancelist:
            unsortedperformancekeys.append(key)

        if len(unsortedperformancekeys) >= 500:
            sortedperformancekeys = radix_sort(unsortedperformancekeys)
        else:
            sortedperformancekeys = merge_sort(unsortedperformancekeys)
        
        if sortedperformancekeys[-1] == 256 * len(targettext):
            print(f"Best brain has a fitness of {256 * len(targettext)}, genome generation completed at generation {generation_no}! Translated genome: {performancelist[sortedperformancekeys[-1]][1]}, Filtered output (Only cares if the first bit of ASCII is the target text!): {targettext}")
            targetreached = True
        else:
            if generation_no % 25 == 0:
                o.pack_obj(generation_no)
                o.pack_obj(gen_size)
                o.pack_obj(generation)
                o.push_bulk()

            bestgenomes = list()
            if generation_no % 100 == 0:
                print(f"Generation {generation_no}, Best Fitness: {sortedperformancekeys[-1]}/{256 * len(targettext)} ({(sortedperformancekeys[-1]/(256 * len(targettext)))*100}%), Best Genome's length: {len(performancelist[sortedperformancekeys[-1]][0])}, Best Filtered output (Only cares if the first bit of ASCII is the target text!): {performancelist[sortedperformancekeys[-1]][2]}")
            elif generation_no % 10 == 0:
                print(f"Generation {generation_no}, Best Fitness: {sortedperformancekeys[-1]}, Best Genome's length: {len(performancelist[sortedperformancekeys[-1]][0])}")
            else:
                print(f"Generation {generation_no}, Best Genome's length: {len(performancelist[sortedperformancekeys[-1]][0])}")

            
            bestgenomes.append(performancelist[sortedperformancekeys[-1]][0])
            bestgenomes.append(performancelist[sortedperformancekeys[-2]][0])
            bestgenomes.append(performancelist[sortedperformancekeys[-3]][0])
            bestgenomes.append(performancelist[sortedperformancekeys[-4]][0])
            bestgenomes.append(performancelist[sortedperformancekeys[-5]][0])

            generation_no += 1

    del o
    print("GENETIC AI STOP")

if __name__ == "__main__":
    path = input('Please input save state path: ') # /Volumes/Data stuffs/Python/AI (New)/Genetic_1/save_state.o2f
    tgt = input('Please input target text (recommended to be short and lowercase for program to not take a million years): ') # hi
    mgl = int(input('Please input max genome (mini-program) length: ')) # 500
    gensz = int(input('Please input generation size (no. of genomes): ')) # 100
    AI(path, tgt, mgl, gensz)