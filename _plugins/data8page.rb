=begin

This Jekyll plugin installs a new Liquid tag to note that our page has text from the UCB data8 original.

Use with:

{% data8page page_name %}

where "page_name" is the name of the page in the data8 site.

=end
require "jekyll"

class Data8Page < Liquid::Tag

    def initialize(tagname, markup, tokens)
        @markup = markup.strip
        super
    end

    def render(context)
        if @markup.empty?
            return "Error processing input, expected syntax: {% data8page name %}"
        end

        # Render the markup
        parameters = Liquid::Template.parse(@markup).render context
        parameters.strip!

        <<EOT
<div class="isa_info">
<i class="fa fa-info-circle"></i>
This page has content from the
<a href="https://github.com/data-8/textbook/blob/64b20f0/notebooks/#{parameters}.ipynb">
#{parameters}</a>
notebook from the UC Berkeley course.  See the Berkeley course section of the
<a href="#{context.registers[:site].config['baseurl']}/license">license</a>
</div>
EOT
    end

    Liquid::Template.register_tag("data8page", self)
end
