using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Random;
namespace Juste_prix
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Random al = new Random();
            int aleatoire = al.Next(0, 101);
            Console.WriteLine(aleatoire);
        }
    }
}
