# frozen_string_literal: true

require 'benchmark'
require 'debug'

class Base
  def run
    run_part_1
    run_part_2
  end

  def run_part_1
    puts "Part 1: #{self.part_1}"
  end

  def run_part_2
    puts "Part 2: #{self.part_2}"
  end

  def benchmark
    Benchmark.bmbm do |x|
      x.report('part 1:') { puts self.part_1 }
      x.report('part 2:') { puts self.part_2 }
    end
  end
end
