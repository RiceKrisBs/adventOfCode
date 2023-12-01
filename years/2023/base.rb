# frozen_string_literal: true

require 'benchmark'

class Base
  def run
    puts "Part 1: #{self.part_1}"
    puts "Part 2: #{self.part_2}"
  end

  def benchmark
    Benchmark.bmbm do |x|
      x.report('part 1:') { puts self.part_1 }
      x.report('part 2:') { puts self.part_2 }
    end
  end
end
