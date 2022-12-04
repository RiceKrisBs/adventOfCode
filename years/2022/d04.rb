# frozen_string_literal: true

testing = false
day = '04'

if testing
  f_input = File.join('inputs', "input#{day}-test.txt")
else
  f_input = File.join('inputs', "input#{day}.txt")
end

def part1(input)
  pairs = []
  File.foreach(input) { |pair| pairs << pair.chomp.split(',') }
  count = 0

  pairs.each do |elf1, elf2|
    e1a, e1b = elf1.split('-').map(&:to_i)
    e1range = e1a..e1b

    e2a, e2b = elf2.split('-').map(&:to_i)
    e2range = e2a..e2b

    count += 1 if e1range.cover?(e2range) || e2range.cover?(e1range)
  end

  count
end

puts("Part 1: #{part1(f_input)}")

def part2(input)
  pairs = []
  File.foreach(input) { |pair| pairs << pair.chomp.split(',') }
  count = 0

  pairs.each do |elf1, elf2|
    e1a, e1b = elf1.split('-').map(&:to_i)
    e1range = e1a..e1b

    e2a, e2b = elf2.split('-').map(&:to_i)
    e2range = e2a..e2b

    count += 1 if e1range.include?(e2a) || e1range.include?(e2b) || e2range.include?(e1a) || e2range.include?(e1b)
  end

  count
end

puts ("Part 2: #{part2(f_input)}")
