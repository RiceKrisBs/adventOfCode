# frozen_string_literal: true

testing = true
day = '01'

if testing
  f_input = File.join('inputs', "input#{day}-test.txt")
else
  f_input = File.join('inputs', "input#{day}.txt")
end

def part_one(input)
  File.foreach(input).with_index do |line, line_num|
    line = line.chomp
  end
end

puts("Part 1: #{part_one(f_input)}")
