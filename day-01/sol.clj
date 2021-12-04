#!/usr/bin/env bb

(ns day1
  (:require
    [clojure.string :as str]
  )
)


(defn part1 [input]
  (count (filter true? (map > (rest input) input))))


(defn part2 [input]
  (count (filter true? (map > (drop 3 input) input))))


(defn parse-input [s]
  (map
    #(Integer/parseInt %)
    (str/split s #"\s")
  )
)


(def example-input
  (parse-input
    "199 200 208 210 200 207 240 269 260 263"
  )
)

(def my-input (parse-input (slurp "input.txt")))


(prn (part1 example-input) 7)
(prn (part2 example-input) 5)
(prn (part1 my-input) 1266)
(prn (part2 my-input) 1217)
