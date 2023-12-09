# frozen_string_literal: true

require_relative 'base'

class Day < Base
  def part_1
    data = File.read(input).split("\n").map(&:split).map { |x| x.map(&:to_i) }
    data.map do |line|
      line.last + find_next_difference(line)
    end.sum
  end

  def part_2
    data = File.read(input).split("\n").map(&:split).map { |x| x.map(&:to_i) }
    data.map do |line|
      line.first - find_first_difference(line)
    end.sum
  end

  private

  TESTING = false
  DAY = '09'
  
  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end

  def find_next_difference(arr)
    differences = find_differences(arr)
    return 0 if differences.all?(&:zero?)
    differences.last + find_next_difference(differences)
  end

  def find_first_difference(arr)
    differences = find_differences(arr)
    return 0 if differences.all?(&:zero?)
    differences.first - find_first_difference(differences)
  end

  def find_differences(arr)
    arr.each_cons(2).map { |a, b| b - a }
  end
end

Day.new.run
# Day.new.benchmark
