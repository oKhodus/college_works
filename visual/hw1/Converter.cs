using System;

class Converter
{
    static void Main(string[] args)
    {
        string invitation_text =
            @"Here is the list of converter options: 
    1. Convert from °C to °F 
    2. Convert from °F to °C

Choose option from 1 to 2: ";
        Console.Write(invitation_text);
        int input_option = Convert.ToInt32(Console.ReadLine());
        switch (input_option)
        {
            case 1:
                Console.Write("Enter value of temperature in Celsius: ");
                string input_celsius = Console.ReadLine();
                double celsius_converted = Convert.ToDouble(input_celsius);
                double fahrenheit_calc = (celsius_converted * 9 / 5) + 32;
                Console.WriteLine($"Temperature in Fahrenheit: {fahrenheit_calc}°");
                break;
            case 2:
                Console.Write("Enter value of temperature in Fahrenheit: ");
                string input_fahr = Console.ReadLine();
                double fahrenheit_converted = Convert.ToDouble(input_fahr);
                double celsius_calc = (fahrenheit_converted - 32) * 5/9;
                Console.WriteLine($"Temperature in Celsius: {celsius_calc}°");
                break;
        }
    }
}


// °F = (°C × 9/5) + 32 option 1.
// °C = (°F - 32) × 5/9 option 2.