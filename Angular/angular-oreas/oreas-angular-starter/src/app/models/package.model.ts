export interface TravelPackage {
  id: string;
  title: string;
  description: string;
  price: number;
  includes: string[];
  featured?: boolean;
}
