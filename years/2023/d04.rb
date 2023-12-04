# frozen_string_literal: true

require_relative 'base'

class Day < Base
  def part_1
    score = 0
    data = File.read(input).split("\n")
    data.map do |line|
      line_data = PATTERN.match(line)
      card_number, winning_numbers, my_numbers = line_data.captures.map(&:split)
      count = my_numbers.filter { |my_num| winning_numbers.include?(my_num) }.count
      next if count == 0
      score += 2 ** (count - 1)
    end
    score
  end

  def part_2
    card_counts = {1 => 1}
    data = File.read(input).split("\n")
    data.map do |line|
      line_data = PATTERN.match(line)
      card_number, winning_numbers, my_numbers = line_data.captures.map(&:split)
      card_number = card_number.first.to_i
      card_counts[card_number] ||= 1
      count = my_numbers.filter { |num| winning_numbers.include?(num) }.count
      next if count == 0
      1.upto(count) do |i|
        card_counts[card_number+i] ||= 1
        card_counts[card_number+i] += card_counts[card_number]
      end
    end
    card_counts.values.sum
  end

  private

  TESTING = false
  DAY = '04'
  PATTERN = /(?<card_num>\d+):(?<winning_nums>.+)\|(?<my_nums>.+)/
  
  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end
end

Day.new.run
# Day.new.benchmark
