# frozen_string_literal: true

testing = true
day = '01'

if testing
  f_input = File.join('inputs', "input#{day}-test.txt")
else
  f_input = File.join('inputs', "input#{day}.txt")
end

def part1(input)
  data = []
  File.foreach(input) { |line| data << line.chomp }
  end
end

puts("Part 1: #{part1(f_input)}")
