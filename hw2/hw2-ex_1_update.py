def main(inp="Enter the number of points: "):
    message_if_out_range = "You cannot obtain {} points"
    message_if_in_range = "The obtained points are {} to be considered for admission"
    try:
        score_inp = float(input(inp).replace(",", "."))
        if 66 <= score_inp <= 100:
            print(message_if_in_range.format("enough"))
        elif 0 <= score_inp < 66:
            print(message_if_in_range.format("not enough"))
        elif score_inp < 0:
            print(message_if_out_range.format("negative"))
        else:
        # elif score_inp > 100
            print(message_if_out_range.format("so many"))
    except ValueError:
        incorrect_inp = "Invalid input, please enter a valid number: "
        main(inp=incorrect_inp)
main()