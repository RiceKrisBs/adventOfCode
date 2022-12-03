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
    compartment1.each_char do |char|
      is_shared = compartment2.include? char
      priorities_sum += letter_score(char) if is_shared
      break if is_shared
    end
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
    grouping = rucksacks[index...index+3]
    grouping[0].each_char do |char|
      letter_presence = grouping.map{ |rucksack| rucksack.include?(char) }
      priorities_sum += letter_score(char) unless letter_presence.include? false
      break unless letter_presence.include? false
    end
    index += 3
  end

  priorities_sum
end

puts("Part 2: #{part2(f_input)}")
