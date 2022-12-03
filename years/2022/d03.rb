# frozen_string_literal: true

testing = false
day = '03'

if testing
  f_input = File.join('inputs', "input#{day}-test.txt")
else
  f_input = File.join('inputs', "input#{day}.txt")
end

def part1(input)
  rucksacks = []
  File.foreach(input) { |line| rucksacks << line.chomp }
  priorities_sum = 0
  rucksacks.each do |rucksack|
    compartment1, compartment2 = rucksack.chars.each_slice(rucksack.length / 2).map(&:join)
    common_letter = (compartment1.chars & compartment2.chars)[0]
    priorities_sum += letter_score(common_letter)
  end

  priorities_sum
end

def letter_score(char)
  char <= 'Z' ? char.ord - 38 : char.ord - 96
end

puts("Part 1: #{part1(f_input)}")

def part2(input)
  rucksacks = []
  File.foreach(input) { |line| rucksacks << line.chomp }
  priorities_sum = 0
  index = 0
  while index < rucksacks.length do
    rucksack1, rucksack2, rucksack3 = rucksacks[index...index+3]
    common_letter = (rucksack1.chars & rucksack2.chars & rucksack3.chars)[0]
    priorities_sum += letter_score(common_letter)
    index += 3
  end

  priorities_sum
end

puts("Part 2: #{part2(f_input)}")
