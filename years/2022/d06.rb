# frozen_string_literal: true

require 'set'
testing = false
day = '06'

if testing
  f_input = File.join('inputs', "input#{day}-test.txt")
else
  f_input = File.join('inputs', "input#{day}.txt")
end


def part1(input)
  data = []
  File.foreach(input) { |line| data << line.chomp }
  datastream = data[0]

  marker_index(datastream, 4)
end

def marker_index(datastream, sequence_length)
  (sequence_length..datastream.length).each do |idx|
    marker = datastream[(idx-sequence_length)...idx]
    set_count = marker.split('').to_set.length
    return idx if set_count == sequence_length
  end
end

puts("Part 1: #{part1(f_input)}")


def part2(input)
  data = []
  File.foreach(input) { |line| data << line.chomp }
  datastream = data[0]

  marker_index(datastream, 14)
end

puts("Part 2: #{part2(f_input)}")
