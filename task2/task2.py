import csv


class Product:
    output_file = 'task2_op.csv'
    input_file = 'product_data.csv'
    output_header = ['Product-Name', 'Product-CostPrice', 'Product-SalesTax-Percentage' , 'Country', 'Product-FinalPrice']

    def price_calculator(self,cost,tax):
        return int(cost) + int(cost) * (tax/100)

    def product_read(self):
        with open(self.input_file) as csv_file:
            data = csv.reader(csv_file,delimiter=',')
            next(data)
            output_list = []
            for row in data:
                output_list.append([row[0], row[1], row[2], row[3], self.price_calculator(row[1], int(row[2]))])
            return output_list


    def product_write(self):
        result = self.product_read()
        with open(self.output_file,'w') as output:
            output_data = csv.writer(output)
            result.insert(0, self.output_header)
            output_data.writerows(result)

if __name__== "__main__":
    Product().product_write()
