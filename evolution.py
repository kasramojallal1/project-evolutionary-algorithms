import copy

from player import Player
import numpy as np
from config import CONFIG


class Evolution():

    def __init__(self, mode):
        self.mode = mode
        self.generation_number = 1

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        # child: an object of class `Player`
        random_number_array = np.random.uniform(low=0, high=1, size=4)
        if random_number_array[0] < 0.2:
            child.nn.w1 = child.nn.w1 + np.random.normal(size=child.nn.w1.shape)
        if random_number_array[1] < 0.2:
            child.nn.w2 = child.nn.w2 + np.random.normal(size=child.nn.w2.shape)
        if random_number_array[2] < 0.2:
            child.nn.b2 = child.nn.b2 + np.random.normal(size=child.nn.b2.shape)
        if random_number_array[3] < 0.2:
            child.nn.b3 = child.nn.b3 + np.random.normal(size=child.nn.b3.shape)


    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            probability_array = []
            cumulative_probabilities = []
            selected_parents = []

            sum_fitness = 0
            for i in range(len(prev_players)):
                sum_fitness += prev_players[i].fitness

            for i in range(len(prev_players)):
                probability_array.append(prev_players[i].fitness / sum_fitness)

            sum_probability = 0
            for i in range(len(probability_array)):
                sum_probability += probability_array[i]
                cumulative_probabilities.append(sum_probability)

            random_numbers = np.random.uniform(low=0, high=1, size=num_players)
            for i in range(len(random_numbers)):
                rand_num = random_numbers[i]
                for j in range(len(cumulative_probabilities)):
                    if rand_num <= cumulative_probabilities[j]:
                        selected_parents.append(prev_players[j])
                        break


            children = []

            # for selected_parent in selected_parents:
            #     child = copy.deepcopy(selected_parent)
            #     children.append(child)

            for i in range(0, len(selected_parents), 2):
                child1 = Player(mode=self.mode)
                child2 = Player(mode=self.mode)

                size_child_w1 = int(child1.nn.w1.shape[0]/2)
                size_child_w2 = int(child1.nn.w2.shape[0]/2)
                size_child_b2 = int(child1.nn.b2.shape[0]/2)
                size_child_b3 = int(child1.nn.b3.shape[0]/2)

                child1.nn.w1[0:size_child_w1, :] =\
                    selected_parents[i].nn.w1[0:size_child_w1, :]
                child2.nn.w1[0:size_child_w1, :] =\
                    selected_parents[i + 1].nn.w1[0:size_child_w1, :]
                child1.nn.w1[size_child_w1:, :] =\
                    selected_parents[i + 1].nn.w1[size_child_w1:, :]
                child2.nn.w1[size_child_w1:, :] =\
                    selected_parents[i].nn.w1[size_child_w1:, :]

                child1.nn.w2[0:size_child_w2, :] = \
                    selected_parents[i].nn.w2[0:size_child_w2, :]
                child2.nn.w2[0:size_child_w2, :] = \
                    selected_parents[i + 1].nn.w2[0:size_child_w2, :]
                child1.nn.w2[size_child_w2:, :] = \
                    selected_parents[i + 1].nn.w2[size_child_w2:, :]
                child2.nn.w2[size_child_w2:, :] = \
                    selected_parents[i].nn.w2[size_child_w2:, :]

                child1.nn.b2[0:size_child_b2, :] = \
                    selected_parents[i].nn.b2[0:size_child_b2, :]
                child2.nn.b2[0:size_child_b2, :] = \
                    selected_parents[i + 1].nn.b2[0:size_child_b2, :]
                child1.nn.b2[size_child_b2:, :] = \
                    selected_parents[i + 1].nn.b2[size_child_b2:, :]
                child2.nn.b2[size_child_b2:, :] = \
                    selected_parents[i].nn.b2[size_child_b2:, :]

                child1.nn.b3[0:size_child_b3, :] = \
                    selected_parents[i].nn.b3[0:size_child_b3, :]
                child2.nn.b3[0:size_child_b3, :] = \
                    selected_parents[i + 1].nn.b3[0:size_child_b3, :]
                child1.nn.b3[size_child_b3:, :] = \
                    selected_parents[i + 1].nn.b3[size_child_b3:, :]
                child2.nn.b3[size_child_b3:, :] = \
                    selected_parents[i].nn.b3[size_child_b3:, :]

                children.append(child1)
                children.append(child2)


            for child in children:
                self.mutate(child)

            # num_players example: 150
            # prev_players: an array of `Player` objects

            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover

            return children

    def next_population_selection(self, players, num_players):

        # num_players example: 100
        # players: an array of `Player` objects

        # TODO (additional): a selection method other than `top-k`
        # TODO (additional): plotting

        sorted_players = sorted(players, key=lambda player_selected: player_selected.fitness)
        sorted_players = sorted_players[-num_players:]

        # f = open("learning_curve.txt", "a")
        # f.write(str(self.generation_number) + ':'
        #         + str(sorted_players[0].fitness) + ':' + str(sorted_players[-1].fitness) + ':'
        #         + str(int(np.mean([my_player.fitness for my_player in sorted_players]))) + ',')
        # f.close()

        self.generation_number += 1

        return sorted_players


