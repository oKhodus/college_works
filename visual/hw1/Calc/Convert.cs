namespace Calc
{
    public static class CalcAndConv
    {
        public static double CelsiusToFahrenheit(double c)
        {
            return (c * 9 / 5) + 32;
        }
        public static double FahrenheitToCelsius(double f)
        {
            return (f - 32) * 5 / 9;
        }
    }
}
