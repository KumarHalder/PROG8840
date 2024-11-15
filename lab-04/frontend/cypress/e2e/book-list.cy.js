describe("Book List", () => {
  beforeEach(() => {
    cy.visit("http://localhost:3000");
  });

  it("should display the book list", () => {
    cy.get("table").should("be.visible");
    cy.get("table tr").should("have.length", 4);
  });

  it("should display the book details", () => {
    cy.get("table tr")
      .eq(1)
      .within(() => {
        cy.get("td").eq(0).should("contain", "1");
        cy.get("td").eq(1).should("contain", "Book 1");
        cy.get("td").eq(2).should("contain", "Author 1");
      });
  });

  it("should delete a book", () => {
    cy.get("table tr")
      .eq(1)
      .within(() => {
        cy.get("button").click();
      });
    cy.get("table tr").should("have.length", 3);
  });

  it("should not display the deleted book", () => {
    cy.get("table tr")
      .eq(1)
      .within(() => {
        cy.get("td").eq(0).should("not.contain", "1");
        cy.get("td").eq(1).should("not.contain", "Book 1");
        cy.get("td").eq(2).should("not.contain", "Author 1");
      });
  });
});
