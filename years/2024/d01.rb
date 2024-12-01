# frozen_string_literal: true

require_relative 'base'

class Day < Base
  def part_1
    data = File.read(input).split("\n")
    left = []
    right = []
    data.map do |line|
      left_num, right_num = line.split.map(&:to_i)
      left << left_num
      right << right_num
    end

    left.sort!
    right.sort!

    left.zip(right).map { |l, r| (l - r).abs }.sum
  end

  def part_2
    data = File.read(input).split("\n")
    left = []
    right = Hash.new(0)
    data.map do |line|
      left_num, right_num = line.split.map(&:to_i)
      left << left_num
      right[right_num] += 1
    end

    left.map { |l| l * (right[l] || 0) }.sum
  end

  private

  TESTING = false
  DAY = '01'

  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end
end

Day.new.run_part_1
Day.new.run_part_2
# Day.new.benchmark
